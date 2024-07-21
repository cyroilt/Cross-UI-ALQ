import tkinter as tk

import sys

sys.path.append("...")
sys.path.append("..")  # Add current directory to PYTHONPATH for importing modules
from Cross_UI_ALQ import Events
from . import Formats as formater
from . import Window as windows
from PIL import Image as img
from PIL import ImageTk as imgtk
from PIL import ImageDraw as imgdrw
class Button():
    def __init__(self,window:windows.Window,position=(0,0),style=None,background=formater.Color(),text="Button",size=(100,50),onclick=None):
        self.window=window
        self.style=style
        self.background=background
        self.text=text
        self.size=size
        self.canvas=self.window.backdrop
        self.position=position
        self.onclick=onclick
        self.events=[]
        self.Tree={"name": "Button", "children": [], "object": self}
    def add(self):
        self.but_background=self.canvas.create_image(self.position[0]+self.size[0]/2,self.position[1]+self.size[1]/2,image=self.background.add_to_canvas())
        self.text_but=self.canvas.create_text(self.position[0]+self.size[0]/2,self.position[1]+self.size[1]/2,text=self.text)

        self.Tree["children"].append({"name": "text", "children": [], "object": self.text_but})
        self.window.__add_child__(self)
        if self.onclick!=None:
            self.canvas.tag_bind(self.but_background,"<Button-1>",lambda event, widget=self: widget.onclick(event))
        self.canvas.tag_bind(self.but_background,"<Enter>",lambda event: print(event))
    def configure(self,position=None,style=None,background=None,text=None,size=None,onclick=None):
        if style != None:
            self.style=style
        if background!= None:
            self.background=background
        if text!=None:
            self.text=text
        if size!=None:
            self.size=size
        if position!=None:
            self.position=position
        if onclick!=None:
            self.onclick=onclick
        
        self.canvas.itemconfig(self.but_background,image=self.background.add_to_canvas())
        self.canvas.moveto(self.but_background,self.position[0],self.position[1])
        self.canvas.itemconfig(self.text_but,text=self.text)
        self.canvas.moveto(self.text_but,self.position[0],self.position[1])
        for i in self.events:
            ev_name=i.event_name
            ev_command=i.command
            self.unbind(ev_name)
            self.bind(ev_name,ev_command)
    def bind(self,EventName,EventCommand):
        self.events.append(Events.Event(self,EventName,EventCommand))
        self.canvas.tag_bind(self.but_background,self.events[-1].association,self.events[-1].on_call)
    def unbind(self,EventName):
        for i in range(len(self.events)):
            if self.events[i].event_name==EventName:
                self.canvas.tag_unbind(self.but_background,self.events[i].association)
                del self.events[i]
                break
        