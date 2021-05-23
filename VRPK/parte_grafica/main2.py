from kivy.app import App
from kivy.uix.button import Button
from kivy.lang.builder import Builder

Builder.load_string("""
<Btn>:
    text: 'Olá Mundo!'


""")

class Btn(Button):
    ...


class MyApp(App):
    def build(
        self
    ):
        return Btn()

if __name__  == '__main__':
    MyApp().run()
