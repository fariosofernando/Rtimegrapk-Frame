from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang.builder import Builder
from kivy.clock import Clock
import os


file = os.listdir()


class Content(ScreenManager):
    def __init__(
        self, **kwargs
        ):
        super(Content, self).__init__(**kwargs)
        
class Projeto(App):
    def build(
        self
    ):
        return Content()

if __name__ == '__main__':
    Projeto().run()
    

