from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.theming import ThemableBehavior
from kivy.clock import mainthread
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import MDList
from kivymd.uix.label import MDLabel
from kivy.uix.popup import Popup
from kivymd.uix.scrollview import MDScrollView
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout

########################################################################
# This is the main presenter which defines a couple reusable functions #
class Presenter(ThemableBehavior, MDScreen):
    ####################################
    # Functions not used to update GUI #

    ###################################
    # Functions used for updating GUI #
    @mainthread
    def setStatus(self, text, color):
        app = MDApp.get_running_app()
        app.setStatus(text, color)

    @staticmethod
    def hide_widget(wid, dohide=True):
        if hasattr(wid, 'saved_attrs'):
            if not dohide:
                wid.height, wid.size_hint_y, wid.opacity, wid.disabled = wid.saved_attrs
                del wid.saved_attrs
        elif dohide:
            wid.saved_attrs = wid.height, wid.size_hint_y, wid.opacity, wid.disabled
            wid.height, wid.size_hint_y, wid.opacity, wid.disabled = 0, None, 0, True

    @staticmethod
    def softHide(wid, dohide=True):
        if hasattr(wid, 'saved_attrs'):
            if not dohide:
                wid.opacity, wid.disabled = wid.saved_attrs
                del wid.saved_attrs
        elif dohide:
            wid.saved_attrs = wid.opacity, wid.disabled
            wid.opacity, wid.disabled = 0, True

    @property
    def app(self):
        return MDApp.get_running_app()

####################################
# Main presenter class for MDLists #
class ListPresenter(ThemableBehavior, MDList):
    MAX_CHILDREN = 10

    @mainthread
    def cleanList(self):
        for i in range(len(self.children)-1,-1,-1):
            self.remove_widget(self.children[i])

    @mainthread
    def addStatus(self, value, color):
        widget = MDLabel(text=value, theme_text_color="Custom")
        widget.text_color = color
        widget.height = "25sp"
        self.add_widget(widget)
        if len(self.children) > self.MAX_CHILDREN:
            self.remove_widget(self.children[-1])
    @mainthread
    def addWidgets(self, widgets):
        # First clean all widgets
        for i in range(len(self.children)-1,-1,-1):
            self.remove_widget(self.children[i])

        for widget in widgets:
            self.add_widget(widget)


class ScrollList(ThemableBehavior, MDScrollView):
    @mainthread
    def addWidget(self, widget):
        self.ids.list.add_widget(widget)

    @mainthread
    def cleanList(self):
        for i in range(len(self.ids.list.children)-1,-1,-1):
            self.ids.list.remove_widget(self.ids.list.children[i])

    @property
    def widgets(self):
        return self.ids.list.children

class TitleLabel(MDLabel):
    pass

class NormalLabel(MDLabel):
    pass

class BigLabel(MDLabel):
    pass

class LabelValue(NormalLabel):
    value_text = StringProperty()
    lbl_text = StringProperty()

class ConfirmPopup(GridLayout):
    text = StringProperty()

    def __init__(self,**kwargs):
        self.register_event_type('on_answer')
        super(ConfirmPopup,self).__init__(**kwargs)

    def on_answer(self, *args):
        pass

class EntryPopup(GridLayout):
    text = StringProperty()
    entry_text = StringProperty()

    def __init__(self,**kwargs):
        self.register_event_type('on_answer')
        super(EntryPopup,self).__init__(**kwargs)

    def on_answer(self, *args):
        pass

class InputDialog(BoxLayout):
    hint_text = StringProperty()
