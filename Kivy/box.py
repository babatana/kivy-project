import io
import os
from kivy.app import App
from kivy.uix.widget import Widget
from Modules.get_data import *
from kivy.properties import ObjectProperty
from kivy.lang import Builder

# Builder.load_file('box.kv')


def print_out():
    print(f"You pressed the label")


# for testing out my buttons
def open_csv():
    # checking if bccm_file.csv has been created
    fd = open("bccm_file.csv", "r")
    check = isinstance(fd, io.IOBase)
    # print("The csv file exists?: ", check)

    """handle the potential error here, in case someone tries to open an empty file"""
    # open the csv file
    os.startfile('bccm_file.csv')


class TheLayout(Widget):
    pass


class BoxApp(App):
    def build(self):
        return TheLayout()




