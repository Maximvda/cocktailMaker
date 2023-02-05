import os
#os.environ["KIVY_NO_CONSOLELOG"] = "1"
import sys
import logging
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.resources import resource_add_path
from kivy.clock import mainthread
from presenters.selector import Selector

class Main(MDApp):
    def build(self):
        self.title = f"Cocktail maker"
        self.theme_cls.colors['Lime']['500'] = "#90e0ef"
        self.theme_cls.colors['Lime']['200'] = "#ffafcc"
        self.theme_cls.colors['Amber']['500'] = "#a2d2ff"
        self.theme_cls.colors['Amber']['200'] = "#cdb4db"
        self.theme_cls.primary_palette = "Lime"
        self.theme_cls.accent_palette = "Amber"
        self.root = Builder.load_file(
                os.path.join(os.path.join(sys._MEIPASS, 'views'),'main.kv'))

    def on_start(self):
        self.root.ids.selector.init()

if __name__ == "__main__":
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
        resource_add_path(os.path.join(sys._MEIPASS, 'views'))
    else:
        sys._MEIPASS = os.getcwd()

    Main().run()
