import time
import threading
import random
from presenters.presenter import Presenter
from kivymd.uix.card import MDCard
from kivy.clock import mainthread

class Selector(Presenter):
    def init(self):
        self.currentIndex = 0
        with open('cocktails.txt', 'r') as f:
            lines = f.readlines()

        for i in range(16):
            ckLines = lines[i*9:9+i*9]
            self.ids[f"cocktail_{i+1}"].ids.lbl_title.text = ckLines[0].split("Name: ")[-1]

            #self.ids[f"cocktail_{i+1}"].ids.lbl_glass.text = ckLines[3]
            #self.ids[f"cocktail_{i+1}"].ids.lbl_ingredients.text = ckLines[4].replace("[", "").replace("]", "").replace("'", "")
            #self.ids[f"cocktail_{i+1}"].ids.lbl_quantities.text = ckLines[5].replace("[", "").replace("]", "").replace("'", "")
            #self.ids[f"cocktail_{i+1}"].ids.lbl_instructions.text = ckLines[6]

            allText = ckLines[3]
            allText += ckLines[4].replace("[", "").replace("]", "").replace("'", "")
            allText += ckLines[5].replace("[", "").replace("]", "").replace("'", "")
            allText += ckLines[6]

            self.ids[f"cocktail_{i+1}"].ids.lbl_all.text = allText
            self.ids[f"cocktail_{i+1}"].ids.image.source = f"images/{i+1}.jpg"

    def randomise(self):
        threading.Thread(target=self._randomise, daemon=True).start()

    def _randomise(self):
        for i in range(10+random.randint(0, 20)):
            time.sleep(0.02*i)
            self._next()

    @mainthread
    def _next(self):
        self.currentIndex += 1
        self.ids.mycarousel.index = self.currentIndex



class Cocktail(MDCard):
    pass
