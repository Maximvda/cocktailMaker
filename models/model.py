import time
from models.mqtt import Mqtt
import models.logger

class Model:
    def __init__(self):
        self.mqtt = Mqtt('192.168.0.10')

    def makeCocktail(self, number):
        print(number)
        self.mqtt.cocktailRequest("MAC", number)

    def makeCustom(self, amounts):
        print(amounts)
        self.mqtt.customCocktail("MAC", amounts)
