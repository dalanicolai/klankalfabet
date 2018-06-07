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
    words={'a':'Ajax', 'b':'Barcelona', 'c':'Cillessen', 'd':'Dommerd',
           'e':'Einstein', 'f':'Figo', 'g':'Guardiola', 'h':'Henry',
           'i':'Iniesta','j':'Johan Cruijf', 'k':'Kahn', 'l':'Liverpool',
           'm':'Messi', 'n':'Neymar', 'o':'Ozil', 'p':'Puyol',
           'q':'Quaresma', 'r':'Ronaldinho', 's':'Suarez', 't':'Turan',
           'u':'Ufo', 'v':'Valdez', 'w':'Weesp', 'x':'Xavi', 'y':'Yamen',
           'z':'Zidane', 'ou':'Auw', 'oe':'OE, oe, oe', 'ie':'Iiiii',
           'eu':'Euzil', 'ui':'Ui', 'grapje':'Stoer'}

    def on_parent(self, widget, parent):
        if platform == 'android':
            self.Locale = autoclass('java.util.Locale')
            self.PythonActivity = autoclass('org.kivy.android.PythonActivity')
            self.TextToSpeech = autoclass('android.speech.tts.TextToSpeech')
            self.tts = self.TextToSpeech(self.PythonActivity.mActivity, None)

            # self.PythonActivity2 = autoclass('org.renpy.android.PythonActivity')
            self.Context = autoclass('android.content.Context')
            self.activity = self.PythonActivity.mActivity
            self.vibrator = self.activity.getSystemService(self.Context.VIBRATOR_SERVICE)
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


    def playimage(self, text, img):
        if text == 'verrassing':
            self.img_source.source = 'images/verrassing.jpg'
            img.reload()
            if platform == 'android':
                # self.tts.setLanguage(self.Locale.US)
                self.tts.speak(text, self.TextToSpeech.QUEUE_FLUSH, None)
                for i in range(10):
                    self.vibrator.vibrate(100)
                    sleep(0.2)
        elif platform == 'android':
            # self.tts.setLanguage(self.Locale.US)
            self.tts.speak(text, self.TextToSpeech.QUEUE_FLUSH, None)
            if text == 'OE, oe, oe':
                sleep(1)
                for i in range(3):
                    self.vibrator.vibrate(100)
                    sleep(0.2)


    def key_pressed(self, letter, im_but):
        self.img_source.source = ''.join(('images/',letter,'.jpg'))
        self.img_source.reload()
        sound = SoundLoader.load(''.join(('sounds/',letter,'.ogg')))
        sound.play()
        im_but.text=self.words[letter]


class KlankalfabetApp(App):

    def build(self):
        pass


klankalfabet = KlankalfabetApp()

if __name__== '__main__':
    klankalfabet.run()

