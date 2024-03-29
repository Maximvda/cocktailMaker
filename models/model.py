import time
from models.mqtt import Mqtt
import models.logger

class Model:
    def __init__(self):
        self.mqtt = Mqtt('siemieserver.duckdns.org')

    def makeCocktail(self, number):
        self.mqtt.cocktailRequest(number)

    def makeCustom(self, amounts):
        self.mqtt.customCocktail(amounts)

    def upgrade(self):
        self.mqtt.upgrade('5130026339', "3.20", "wallLed.bin")

    def calibrate(self):
        print("Cocktail request 17")
        self.mqtt.cocktailRequest(16)
