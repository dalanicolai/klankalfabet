import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class KlankalfabetApp(App):

    def build(self):
        return GridLayout()

klankalfabet = KlankalfabetApp()

klankalfabet.run()