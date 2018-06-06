import kivy
kivy.require('1.10.0')

import os
from time import sleep

from jnius import autoclass

from kivy.core.audio import SoundLoader
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

from kivy.utils import platform

class MainWindow(BoxLayout):
    # img_source = ObjectProperty(id)

    def img_path(self):
        print(self.img_source.source)


    def playstring(self, text, img):
        if text == '':
            text = "ronaldo is een sukkel"
            img.source = 'images/sukkel.jpg'
            # self.img_source.source = 'images/sukkel.jpg'
            img.reload()
        Locale = autoclass('java.util.Locale')
        if platform == 'android':
            PythonActivity = autoclass('org.renpy.android.PythonActivity')
        TextToSpeech = autoclass('android.speech.tts.TextToSpeech')
        tts = TextToSpeech(PythonActivity.mActivity, None)
        tts.setLanguage(Locale.US)
        tts.speak('Hello World.', TextToSpeech.QUEUE_FLUSH, None)

        # tts.save("good.mp3")
        # os.system("mpg123 good.mp3")

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

