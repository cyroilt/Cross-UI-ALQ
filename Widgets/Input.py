import tkinter as tk
import sys
import sys
import os 
sys.path.append(os.getcwd())
from .Formats import Color
class Input():

    def __init__(self, window,type="Entry", background=Color(),size=(100,100)):
        self.window=window
        self.type=type
        self.__get_root__=window.__get_root__
        self.background=background
        self.size=size
        self.canvas=self.window.backdrop
        self.position=(0,0)
        