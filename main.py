import kivy
kivy.require('1.10.0')

from kivy.core.audio import SoundLoader
from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class KlankalfabetApp(App):

    def build(self):
        return GridLayout()

    def key_pressed(self, letter):
        sound = SoundLoader.load(letter)
        sound.play()

klankalfabet = KlankalfabetApp()

klankalfabet.run()

# domme PyCharm

print("PyCharms is een sukkel")