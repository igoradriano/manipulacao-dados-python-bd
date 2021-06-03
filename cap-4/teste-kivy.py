from kivy.app import App
from kivy.uix.button import Button
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

class ExemploApp(App):
    def build(self):
        return Button(text='Olá, Mundo!')

ExemploApp().run()