from kivy.app import App
from kivy.uix.label import Label

class HelloApp(App):
    def build(self):
        return Label(text='Hello from Kivy!')

HelloApp().run()
