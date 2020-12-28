from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

# Builder.load_file('box.kv')


def print_out():
    print("You pressed a button")


class TheLayout(Widget):
    pass


class BoxApp(App):
    def build(self):
        return TheLayout()




