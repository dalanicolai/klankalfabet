import kivy
kivy.require('1.10.0')

import os
from time import sleep

from jnius import autoclass

from kivy.core.audio import SoundLoader
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import ObjectProperty

from kivy.utils import platform

class MainWindow(BoxLayout):
    # img_source = ObjectProperty(id)
    words={'a','Ajax'}

    def on_parent(self, widget, parent):
        if platform == 'android':
            self.Locale = autoclass('java.util.Locale')
            self.PythonActivity = autoclass('org.kivy.android.PythonActivity')
            self.TextToSpeech = autoclass('android.speech.tts.TextToSpeech')
            self.tts = self.TextToSpeech(self.PythonActivity.mActivity, None)
            # tts.setLanguage(Locale.US)
            # tts.speak(text, TextToSpeech.QUEUE_FLUSH, None)

    def img_path(self):
        print(self.img_source.source)


    def playstring(self, text, img):
        if text == '':
            text = "ronaldo is een sukkel"
            img.source = 'images/sukkel.jpg'
            # self.img_source.source = 'images/sukkel.jpg'
            img.reload()
        if platform == 'android':
            # self.tts.setLanguage(self.Locale.US)
            self.tts.speak(text, self.TextToSpeech.QUEUE_FLUSH, None)

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

