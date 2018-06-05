import kivy
kivy.require('1.10.0')

from gtts import gTTS
import os

from kivy.core.audio import SoundLoader
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

class MainWindow(BoxLayout):
    img_source = ObjectProperty(id)

    def img_path(self):
        print(self.img_source.source)


    def playstring(self, text):
        if text is '':
            text = "ronaldo is een sukkel"
            self.img_source.source = 'images/sukkel.jpg'
            self.img_source.reload()
        tts = gTTS(text, lang='nl')
        tts.save("good.mp3")
        os.system("mpg123 good.mp3")

    def key_pressed(self, letter):
        self.img_source.source = ''.join(('images/',letter,'.jpg'))
        self.img_source.reload()
        sound = SoundLoader.load(''.join(('sounds/',letter,'.ogg')))
        sound.play()

class KlankalfabetApp(App):

    def build(self):
        pass

klankalfabet = KlankalfabetApp()

if __name__== '__main__':
    klankalfabet.run()

