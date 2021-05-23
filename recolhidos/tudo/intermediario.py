from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder
from kivy.clock import Clock
from kivy.uix.button import Button
import random


Builder.load_file('tudo/recepctor_final.kv')


class Catolog(BoxLayout):
    ...

class ScreenOne(Screen):
    def __init__(
        self, **kw
    ):
        super().__init__(**kw)
        Clock.schedule_interval(self.update_name,2)

    def update_name(
        self, dt
    ):  
        self.ids.box.clear_widgets()
        btn = Button()
        self.ids.box.add_widget(btn)
        print(self.children)


class VRPK(App):
    def build(self):
        return Catolog()
VRPK().run()