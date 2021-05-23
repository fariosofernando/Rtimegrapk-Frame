from kivy.app import App
from datetime import datetime
from datetime import timedelta
from kivy.clock import Clock
from kivy.uix.label import Label

class MyApp(App):
    def build(self):


        self.tempo_agora = datetime.now()

        # Schedule the self.update_clock function to be called once a second
        Clock.schedule_interval(self.update_clock, 1) # Loop
        self.my_label = Label(text= self.tempo_agora.strftime('%H:%M:%S'))# O tempo é 16:04:00

        return self.my_label  # The label is the only widget in the interface

    def update_clock(self, *args):
        # Called once a second using the kivy.clock module
        # Add one second to the current time and display it on the label
        self.tempo_agora = self.tempo_agora + timedelta(seconds = 1)
        self.my_label.text = self.tempo_agora.strftime('%H:%M:%S')

MyApp().run()