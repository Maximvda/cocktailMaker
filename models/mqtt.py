import logging
import copy
import os
import paho.mqtt.client as mqtt
import constants as constants
from concurrent.futures import ThreadPoolExecutor
import models.ledWall_pb2 as wificonnect_pb2
from google.protobuf.internal.encoder import _VarintBytes
from google.protobuf.internal.decoder import _DecodeVarint32

TOPICS = [
    "inf/in/short/",
    "inf/in/long/",
    "inf/in/debug/",
    "inf/in/event/",
    "inf/out/",
    "inf/in/status/",
]

# Mqtt client to decode protobuf
class Mqtt(mqtt.Client):
    _MACs = []
    # All different protobuf variables
    _command = wificonnect_pb2.Command()

    # Initialse the client
    def __init__(self, url, user=None, password=None, port=1883, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Init logging
        self._logger = logging.getLogger("Mqtt client")
        self._url = url
        # Set paasword and connect the loop
        try:
            self.username_pw_set(user, password=password)
            self.connect_async(url, port)
            self.loop_start()
            self._logger.info("Mqtt loop started")
        except TimeoutError:
            self._logger.error(f"Failed to connect to: {url}")

        # Setting up threadpool executer to process incomming messages
        self._executor = ThreadPoolExecutor(max_workers=8)

    # Initialiser from farm
    @classmethod
    def from_farm(cls, farm):
        url = constants.FARM_URL[farm]
        user = constants.FARM_USER[farm]
        password = constants.FARM_USER[farm]
        port = constants.FARM_PORT[farm]
        return cls(url, user, password, port)

    # Start subscription when client is connected
    def on_connect(self, client, userdata, flags, rc):
        self._logger.info(f"Connected to: {self._url}")
        if hasattr(self, "cb_connected"):
            self.cb_connected()
        for MAC in self._MACs:
            for topic in TOPICS:
                self.subscribe(f"{topic}{MAC}")

    def on_disconnect(self, client, userdata, rc):
        self._logger.warning("Disconnected!!")

    def on_subscribe(self, _client, _userdata, mid, _qos):
        if hasattr(self, "cb_onSubscribe"):
            self.cb_onSubscribe(mid)
    def on_unsubscribe(self, _client, _userdata, mid):
        if hasattr(self, "cb_unSubscribe"):
            self.cb_unSubscribe(mid)

    # Add new MAC to communicate through mqtt client
    def addMAC(self, MAC):
        self._logger.info(f"Subscribing: {MAC}")
        self._MACs.append(MAC)
        for topic in TOPICS:
            res = self.subscribe(f"{topic}{MAC}")
        return res

    def removeMAC(self, MAC):
        self._logger.info(f"Unsubscribing: {MAC}")
        if MAC in self._MACs:
            self._MACs.remove(MAC)
        for topic in TOPICS:
            res = self.unsubscribe(f"{topic}{MAC}")
        return res

    def cocktailRequest(self, cocktail):
        request = wificonnect_pb2.Command()
        request.cocktail.cocktail = cocktail+1
        self._sendCommand(request)

    def customCocktail(self, amounts):
        request = wificonnect_pb2.Command()
        request.cocktail.amaretto = amounts[0]
        request.cocktail.lime = amounts[1]
        request.cocktail.brandy = amounts[2]
        request.cocktail.rum = amounts[3]
        request.cocktail.triple_sec = amounts[4]
        self._sendCommand(request)

    def upgrade(self, serial, version, file):
        self._logger.info(f"Upgrading: {serial}  to version: {version}")
        command = wificonnect_pb2.Command()
        command.upgrade.deviceType = int(serial[0:4])
        if serial.startswith("5130") or serial.startswith("5110"):
            command.upgrade.firmWareMajorVersion = 1
            command.upgrade.firmWareMinorVersion = 0
        else:
            command.upgrade.serialNumbers.extend([int(serial[4:])])
        command.upgrade.imageSize = int(os.path.getsize(file)) # in bytes
        with open(file, 'rb') as f:
            data = f.read()
        self._sendUpgrade(command, data)

    # Queue the incomming messages for decoding
    def on_message(self, _Client, _userdata, message):
        if hasattr(self, "cbMessage"):
            self._executor.submit(
                self.cbMessage, *[message.topic, message.payload]
            )

        self._executor.submit(self._decodeMessage, message)

    # Decode the message
    def _decodeMessage(self, message):
        (topic, mac) = message.topic.split("/")[-2:]
        payload = message.payload
        self._logger.info(message)

    def _sendCommand(self, command, topic="inf/out"):
        self.publish(f"espWall/command", command.SerializeToString(), qos=0, retain=False)

    def _sendUpgrade(self, command, data):
        encodedCommand = _VarintBytes(command.ByteSize()) + command.SerializeToString()
        encodedCommand += data
        self.publish(f"espWall/command", encodedCommand, qos=1, retain=False)
