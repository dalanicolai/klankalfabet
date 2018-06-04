import kivy
kivy.require('1.10.0')

from gtts import gTTS
import os

from kivy.core.audio import SoundLoader
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.image import Image

class KlankalfabetApp(App):
    # img_source = 'images/art.png'

    def build(self):
        return BoxLayout()

    def key_pressed(self, letter):
        sound = SoundLoader.load(letter)
        sound.play()

    def playstring(self, text):
        if text is '':
            text = "ronaldo is een sukkel"
        tts = gTTS(text, lang='nl')
        tts.save("good.mp3")
        os.system("mpg123 good.mp3")
        return

klankalfabet = KlankalfabetApp()

if __name__== '__main__':
    klankalfabet.run()

