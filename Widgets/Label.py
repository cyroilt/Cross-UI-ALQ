import tkinter as tk
from . import Formats as formater
from . import Window as windows
from PIL import Image as img
from PIL import ImageTk as imgtk
from PIL import ImageDraw as imgdrw
class Label():
    def __init__(self,window:windows.Window, position=(0,0), style=None, background=formater.Color(), text="Label", size=(100,50), font=("Arial",12)):
        self.window=window
        self.style=style
        self.background=background
        self.text=text
        self.size=size
        self.font=font
        self.canvas=self.window.backdrop
        self.position=position
        
        self.Tree={"name": "Label", "children": [], "object": self}
    
    def add(self):
        self.window.__add_child__(self)
        self.label_bg=self.canvas.create_image(self.position[0]+self.size[0]/2,self.position[1]+self.size[1]/2,image=self.background.add_to_canvas())
        self.label_text=self.canvas.create_text(self.position[0]+self.size[0]/2,self.position[1]+self.size[1]/2,text=self.text)