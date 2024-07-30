import tkinter as tk
from . import Formats as formater
from . import Window as windows
from PIL import Image as img
from PIL import ImageTk as imgtk
from PIL import ImageDraw as imgdrw
class Label():
    def __init__(self,window:windows.Window, position=(0,0), style=None, background=formater.Color(size_of_area=(200,200)), text="Label", size=(100,50),foreground:formater.Color|formater.LinearGradient|formater.RadialGradient=None, font=("arial",15)):
        self.window=window
        self.style=style
        self.background=background
        self.text=text
        self.size=size
        self.__get_root__=window.__get_root__
        self.font=font
        self.canvas=self.window.backdrop
        self.position=position
        self.foreground=foreground
        self.Tree={"name": "Label", "children": [], "object": self}
    
    def add(self):
        self.window.__add_child__(self)
        self.label_bg=self.canvas.create_image(self.position[0]+self.size[0]/2,self.position[1]+self.size[1]/2,image=self.background.add_to_canvas())
        if self.foreground==None:
            self.label_text=self.canvas.create_text(self.position[0]+self.size[0]/2,self.position[1]+self.size[1]/2,text=self.text)
        else:
            self.fforeground=formater.Foreground(text=self.text,for_object=self.foreground,font=self.font)
            self.label_text=self.canvas.create_image(self.position[0]+self.size[0]/2,self.position[1]+self.size[1]/2,image=self.fforeground.add_to_canvas())

    
    def configure(self, position=None, style=None, background=None, text=None, size=None, font=None):
        if position!=None:
            self.position=position
            self.canvas.move(self.label_bg, *self.position)
            self.canvas.move(self.label_text, *self.position)
        if style!=None:
            self.style=style
        if background!=None:
            self.background=background
            self.canvas.itemconfig(self.label_bg, image=self.background.add_to_canvas())
        if text!=None:
            self.text=text
            self.canvas.itemconfig(self.label_text, text=self.text)
        if size!=None:
            self.size=size
            self.canvas.coords(self.label_bg, *self.position, self.position[0]+self.size[0], self.position[1]+self.size[1])
        if font!=None:
            self.font=font
            self.canvas.itemconfig(self.label_text, font=self.font)
    
    def destroy(self):
        self.canvas.delete(self.label_bg)
        self.canvas.delete(self.label_text)
        self.window.__remove_child__(self)
