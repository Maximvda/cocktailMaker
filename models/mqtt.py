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

    def cocktailRequest(self, MAC, cocktail):
        request = wificonnect_pb2.Command()
        request.cocktail.cocktail = cocktail+1
        self._sendCommand(MAC, request)

    def customCocktail(self, MAC, amounts):
        request = wificonnect_pb2.Command()
        request.cocktail.amaretto = amounts[0]
        request.cocktail.lime = amounts[1]
        request.cocktail.brandy = amounts[2]
        request.cocktail.rum = amounts[3]
        request.cocktail.triple_sec = amounts[4]
        self._sendCommand(MAC, request)

    def upgrade(self, MAC, serial, version, file):
        self._logger.info(f"Upgrading: {serial}  to version: {version}")
        command = wificonnect_pb2.Command()
        command.upgrade.deviceType = int(serial[0:4])
        if serial.startswith("5130") or serial.startswith("5110"):
            command.upgrade.firmWareMajorVersion = int(version[0])
            command.upgrade.firmWareMinorVersion = int(version[1])
        else:
            command.upgrade.serialNumbers.extend([int(serial[4:])])
        command.upgrade.imageSize = int(os.path.getsize(file)) # in bytes
        with open(file, 'rb') as f:
            data = f.read()
        self._sendUpgrade(MAC, command, data)

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
        # No callback function so we don't have to decode message
        if not hasattr(self, f"cb_{mac}"):
            return
        # Decode the message with the protobuf
        if topic in ['long', 'short']:
            self._measurement.ParseFromString(payload)
            value = copy.copy(self._measurement)
        elif topic == 'debug':
            value = payload.decode()
        elif topic == 'status':
            self._status.ParseFromString(payload)
            value = copy.copy(self._status)
        elif topic == 'out':
            next_pos, pos = 0, 0
            try:
                while pos < len(payload):
                    next_pos, pos = _DecodeVarint32(payload, pos)
                    msg_buf = payload[pos:pos + next_pos]
                    pos += next_pos
                    self._command.ParseFromString(msg_buf)
                    if self._command.HasField("modbusWrite"):
                        logging.getLogger('Out modbus').info(f"{self._command}")
                    else:
                        logging.getLogger('Out').info(f"{self._command}")
                return
            except:
                self._logger.debug(f"Couldn't decode: {payload}")
                return
        elif topic == 'event':
            value = payload
        else:
            logging.getLogger("Mqtt error").warning(f"Couldn't decode the following: {msg.topic}/{msg.payload}")
            return

        # Log the decoded message
        logging.getLogger(topic.capitalize()).info(f"{value}")
        # Execute the callback function
        eval(f"self.cb_{mac}")(topic, value)

    def sendStatus(self, MAC, status):
        self.publish(f"inf/in/status/{MAC}", status.SerializeToString(), qos=0, retain=False)

    def _sendCommand(self, MAC, command, topic="inf/out"):
        self.publish(f"espWall/command", command.SerializeToString(), qos=0, retain=False)

    def _sendUpgrade(self, MAC, command, data):
        encodedCommand = _VarintBytes(command.ByteSize()) + command.SerializeToString()
        encodedCommand += data
        self.publish(f"inf/out/{MAC}", encodedCommand, qos=1, retain=False)
