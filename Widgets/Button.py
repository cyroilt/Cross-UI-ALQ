import tkinter as tk
import Formats as formater
import Window as windows
from PIL import Image as img
from PIL import ImageTk as imgtk
from PIL import ImageDraw as imgdrw
class Button():
    def __init__(self,window:windows.Window,style=None,background=formater.Color(),text="Button",size=(100,50)):
        self.window=window
        self.style=style
        self.background=background
        self.text=text
        self.size=size