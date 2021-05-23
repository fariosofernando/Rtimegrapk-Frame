import os
import sys
from kivy.app import App
from kivy.factory import Factory
from kivy.lang import Builder, Parser, ParserException
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.animation import Animation
from kivy.uix.textinput import TextInput
from kivy.clock import Clock

# Paths manipulacao
Diretorio_atual = os.path.dirname(__file__) # Diretorio atual
parte_grafica = os.path.join(Diretorio_atual, 'parte_grafica')
parte_grafica_classes = [c[:-3] for c in os.listdir(parte_grafica)
    if c.endswith('.kv')]


class Container(BoxLayout):
    def __init__(self, **kwargs):
        super(Container, self).__init__(**kwargs)

    @property
    def kv_file(self):
        return os.path.join(parte_grafica, self.__class__.__name__ + '.kv')


for class_name in parte_grafica_classes:
    globals()[class_name] = type(class_name, (Container,), {})


class KivyRenderTextInput(TextInput):
    def keyboard_on_key_down(self, window, keycode, text, modifiers):
        is_osx = sys.platform == 'darwin'
        # Keycodes on OSX:
        ctrl, cmd = 64, 1024
        key, key_str = keycode

        if text and key not in (list(self.interesting_keys.keys()) + [27]):
            # This allows *either* ctrl *or* cmd, but not both.
            if modifiers == ['ctrl'] or (is_osx and modifiers == ['meta']):
                if key == ord('s'):
                    self.catalog.change_kv(True)
                    return

        return super(KivyRenderTextInput, self).keyboard_on_key_down(
            window, keycode, text, modifiers)


class Catalog(BoxLayout):

    language_box = ObjectProperty()
    screen_manager = ObjectProperty()
    _change_kv_ev = None

    def __init__(self, **kwargs):
        self._previously_parsed_text = ''
        super(Catalog, self).__init__(**kwargs)
        
        Clock.schedule_interval(self.show_kv, 1)
        self.carousel = None

    def show_kv(self,dt):

        child = self.screen_manager.current_screen.children[0]
        with open(child.kv_file, 'rb') as file:
            self.language_box.text = file.read().decode('utf8')
        if self._change_kv_ev is not None:
            self._change_kv_ev.cancel()
        self.change_kv()
        # reset undo/redo history
        self.language_box.reset_undo()

    def schedule_reload(self):
        if self.auto_reload:
            txt = self.language_box.text
            child = self.screen_manager.current_screen.children[0]
            if txt == child.previous_text:
                return
            child.previous_text = txt
            if self._change_kv_ev is not None:
                self._change_kv_ev.cancel()
            if self._change_kv_ev is None:
                self._change_kv_ev = Clock.create_trigger(self.change_kv)
            self._change_kv_ev()

    def change_kv(self, *largs):

        txt = self.language_box.text
        kv_container = self.screen_manager.current_screen.children[0]
        try:
            parser = Parser(content=txt)
            kv_container.clear_widgets()
            widget = Factory.get(parser.root.name)()
            Builder._apply_rule(widget, parser.root, parser.root)
            kv_container.add_widget(widget)
        except (SyntaxError, ParserException) as e:
            self.show_error(e)
        except Exception as e:
            self.show_error(e)

    def show_error(self, e):
        self.info_label.text = str(e).encode('utf-8')
        self.anim = Animation(top=190.0, opacity=1, d=2, t='in_back') +\
            Animation(top=190.0, d=3) +\
            Animation(top=0, opacity=0, d=2)
        self.anim.start(self.info_label)


class VRPKApp(App):

    def build(self):
        return Catalog()

    def on_pause(self):
        return True


VRPKApp().run()


