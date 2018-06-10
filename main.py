import kivy
kivy.require('1.10.0')

import os
from time import sleep
import random

from jnius import autoclass

from kivy.core.audio import SoundLoader
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import ObjectProperty

from kivy.utils import platform

class MainWindow(BoxLayout):
    element = 'verassing'
    im = ObjectProperty(id)
    im_button = ObjectProperty(id)
    auto_button = ObjectProperty(id)

    words={'a':['appel','aardbei','ananas'], 'b':['banaan','bezem'], 'c':['citroen'], 'd':['druiven'],
           'e':['emmer'], 'f':['fruit'], 'g':['grapefruit','granaatappel'], 'h':['hamer'],
           'i':['italie'],'j':['jas'], 'k':['kiwi','komkommer','kokosnoot'], 'l':['lepel','limoen','lychee'],
           'm':['mes','meloen','mandarijn','mango'], 'n':['nectarine'], 'o':['olijven'], 'p':['peer','pompoen','pan','perzik','paprika'],
           'q':['qubit','quarks','quinoa'], 'r':['rozenbottel','roos'], 's':['sinaasappel'], 't':['tomaat'],
           'u':['ufo'], 'v':['vork','vincent van gogh'], 'w':['wesp'], 'x':['xylofoon'], 'y':['griekse y','yoghurt','yoga'],
           'z':['zakmes'], 'ou':['auw'], 'oe':['oe, oe, oe'], 'ie':['iiiii'],
           'ei':['ei'],'eu':['europa'], 'ui':['ui']}

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
            # tts.setLanguage(Locale.US)l
            # tts.speak(text, TextToSpeech.QUEUE_FLUSH, None)

    # def img_path(self):
    #     print(self.im.source)

    def playimage(self, text, img):
        if text == 'verrassing':
            self.im.source = 'images/verrassing.jpg'
            img.reload()
            if platform == 'android':
                # self.tts.setLanguage(self.Locale.US)
                self.tts.speak(text, self.TextToSpeech.QUEUE_FLUSH, None)
                for i in range(10):
                    self.vibrator.vibrate(100)
                    sleep(0.2)
        elif platform == 'android':
            # self.tts.setLanguage(self.Locale.US)
            self.tts.speak(self.element, self.TextToSpeech.QUEUE_FLUSH, None)
            if text == 'oe, oe, oe':
                sleep(1)
                for i in range(3):
                    self.vibrator.vibrate(100)
                    sleep(0.2)

    def toggle_auto(self, text):
        if text == 'auto: aan':
            self.auto_button.text = 'auto: uit'
        else:
            self.auto_button.text = 'auto: aan'

    def toggle_hide(self, text):
        if text == 'toon':
            self.hide_button.text = 'verstop'
            self.auto_button.text = 'auto: uit'
        else:
            self.hide_button.text = 'toon'

    def playstring(self, text):
        if text == '':
            self.im_button.text = "Sukkel"
            text = "ronaldo is een sukkel"
            self.im.source = 'images/sukkel.jpg'
            # self.im.source = 'images/sukkel.jpg'
            self.im.reload()
        if platform == 'android':
            # self.tts.setLanguage(self.Locale.US)
            self.tts.speak(text, self.TextToSpeech.QUEUE_FLUSH, None)

        # tts.save("good.mp3")
        # os.system("mpg123 good.mp3")

    def key_pressed(self, letter):
        self.element = random.choice(self.words[letter])
        self.im.source = ''.join(('images/',self.element,'.jpg'))
        self.im.reload()
        sound = SoundLoader.load(''.join(('sounds/',letter,'.ogg')))
        sound.play()
        if self.hide_button.text == 'verstop':
            self.im_button.text = '???'
        else:
            self.im_button.text=self.element
        if platform == 'android' and self.auto_button.text == 'auto: aan':
            sleep(1)
            self.tts.speak(self.element, self.TextToSpeech.QUEUE_FLUSH, None)




class KlankalfabetApp(App):

    def build(self):
        pass


klankalfabet = KlankalfabetApp()

if __name__== '__main__':
    klankalfabet.run()

