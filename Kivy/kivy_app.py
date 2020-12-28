from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.uix.dropdown import DropDown
from kivy.base import runTouchApp
from kivy.properties import ObjectProperty
from kivy.lang import Builder

# Builder.load_file('my.kv')


class TheGridLayout(Widget):
    name = ObjectProperty(None)

    # button's function call
    def press(self):
        name = self.name.text
        self.add_widget(Label(text=f'Hello {name}'))
        # clear
        self.name.text = ""


class MyApp(App):
    def build(self):
        return TheGridLayout()


"""
class CanvasWidget(Widget):
    def __init__(self, **kwargs):
        super(CanvasWidget, self).__init__(**kwargs)

        with self.canvas:
            Color(.234, .456, .678, .8)

            self.rect = Rectangle(pos=self.center,
                                  size=(self.width / 2.,
                                        self.height / 2.))
            self.bind(pos=self.update_rect,
                      size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
"""
