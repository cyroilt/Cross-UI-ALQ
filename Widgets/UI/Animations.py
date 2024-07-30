from tkinter import Tk
#from ..Widgets import Formats as palette
#from ..Widgets.Window import Window
import sys
import os 
sys.path.append(os.getcwd())

from .. import Formats as palette
from .. import Window
class AnimationPlayer():
    def __init__(self,fps=10) -> None:
        self.fps=fps
        self.animations=[]
    def add_animation(self,animation):
        self.animations.append(animation)
    def play(self,animation_name):
        for i in self.animations:
            if i.name==animation_name:
                i.play()
    def stop(self,animation_name):
        for i in self.animations:
            if i.name==animation_name:
                i.stop()
class Animation():
    def __init__(self,widget:Window,time=1,parameter_changing="color",from_state=palette.Color(),to_state=palette.Color(color=(255,225,255,255))):
        self.from_state=from_state
        self.to_state=to_state
        self.time=time
        self.name=""
        self.tk_widget=widget
        self.parameter_changing=parameter_changing
        self.current_time=0
        self.fps=widget.__get_root__.__animation__player__.fps
        self.is_playing=False
        self.frames=[]
        if type(self.from_state)!=type(self.to_state):
            raise TypeError(f"Both from_state and to_state should be of the same type {self.from_state} and {self.to_state}")
        self.__precompile__()
    def __precompile__(self):
        if self.parameter_changing=="background":
            if type(self.from_state)==palette.Color:
                delta_r=self.to_state.__color__[0]-self.from_state.__color__[0]
                delta_g=self.to_state.__color__[1]-self.from_state.__color__[1]
                delta_b=self.to_state.__color__[2]-self.from_state.__color__[2]
                delta_a=self.to_state.__color__[3]-self.from_state.__color__[3]
                self.frames=[palette.Color(size_of_area=self.from_state.size,color=(round(self.from_state.__color__[0]+i*delta_r/(self.time*self.fps)),round(self.from_state.__color__[1]+i*delta_g/(self.time*self.fps)),round(self.from_state.__color__[2]+i*delta_b/(self.time*self.fps)),round(self.from_state.__color__[3]+i*delta_a/(self.time*self.fps)))) for i in range (round((self.time*self.fps)+1))]
    def play(self):
        if self.time > self.current_time:
            self.is_playing=True
            
            self.current_time+=1/self.fps
            self.__update_widget__(self.frames[round(self.current_time*self.fps)-1])
            self.tk_widget.__get_root__.backdrop.update()
            self.afterfunc=self.tk_widget.__get_root__.window.after(round(1/self.fps*1000),self.play)
        else:
            self.is_playing=False
            self.stop()
    def __update_widget__(self,what):
        if self.parameter_changing=="background":
            self.tk_widget.configure(background=what)
    def stop(self):
        self.is_playing=False
        self.tk_widget.__get_root__.window.after_cancel(self.afterfunc)
        self.current_time=0
