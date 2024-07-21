from .Formats import *


class Style():
    def __init__(self):
        self.Stylemap = {"Menu": ""}

    def stylemap(self, item):
        return self.Stylemap[item]


class Window():
    def __init__(self, name="MainWindow", background=Color(size_of_area=(800, 600), color=(255, 255, 255, 255))):
        self.window = tk.Tk()
        self.name = name
        self.background=background
        self.projectTree = {"name": self.name, "children": [], "object": self.window}
        self.backdrop = tk.Canvas(self.window,width=self.window.winfo_reqwidth(),bd=0,height=self.window.winfo_reqheight(),background="white")
        self.background = background
        self.last_ev_width = self.window.winfo_reqwidth()
        self.last_ev_height = self.window.winfo_reqheight()
        if type(self.background)==Color:
            self.background=Color(size_of_area=(self.window.winfo_reqwidth(),self.window.winfo_reqheight()),color=self.background.__color__)
            self.bg_color=self.backdrop.create_image(100,100,image=self.background.add_to_canvas())
            print("ok")
        elif type(self.background)==LinearGradient:
            self.background=LinearGradient(size=(self.window.winfo_width(),self.window.winfo_height()),colors=self.background.color_points,rotation=self.background.rotation)
            self.bg_color=self.backdrop.create_image(self.window.winfo_width()//2,self.window.winfo_height()//2, image=self.background.add_to_canvas())
        elif type(self.background)==RadialGradient:
            self.background=RadialGradient(size=(self.window.winfo_width(),self.window.winfo_height()),colors=self.background.color_points,rotation=self.background.rotation,center=self.background.center)
            self.bg_color=self.backdrop.create_image(self.window.winfo_width()//2,self.window.winfo_height()//2, image=self.background.add_to_canvas())
        self.backdrop.place(x=0,y=0)
        self.window.bind("<Configure>",self.__on__RESIZE)
    def __add_child__(self, child):
        self.projectTree["children"].append(child)
    def __on__RESIZE(self,event):
        if event.width!=self.last_ev_width or event.height!=self.last_ev_height:
            self.last_ev_width = event.width
            self.last_ev_height = event.height
        else:
            return 0
        if event.widget==self.window:
            
            self.backdrop.configure(width=event.width,height=event.height)
            if type(self.background)==Color:
                self.background=Color(size_of_area=(self.window.winfo_width(),self.window.winfo_height()),color=self.background.__color__)
                self.backdrop.delete(self.bg_color)
                self.bg_color = self.backdrop.create_image(self.window.winfo_width()//2,self.window.winfo_height()//2, image=self.background.add_to_canvas())
                self.backdrop.tag_lower(self.bg_color)
            elif type(self.background)==LinearGradient:
                self.background=LinearGradient(size=(self.window.winfo_width(),self.window.winfo_height()),colors=self.background.color_points,rotation=self.background.rotation)
                self.backdrop.delete(self.bg_color)
                self.bg_color = self.backdrop.create_image(self.window.winfo_width()//2,self.window.winfo_height()//2, image=self.background.add_to_canvas())
                self.backdrop.tag_lower(self.bg_color)
            elif type(self.background)==RadialGradient:
                self.background=RadialGradient(size=(self.window.winfo_width(),self.window.winfo_height()),colors=self.background.color_points,rotation=self.background.rotation,center=self.background.center)
                self.backdrop.delete(self.bg_color)
                self.bg_color = self.backdrop.create_image(self.window.winfo_width()//2,self.window.winfo_height()//2, image=self.background.add_to_canvas())
                self.backdrop.tag_lower(self.bg_color)
class Menu():
    def __init__(self, window: Window, style=Style().stylemap("Menu")):
        self.menu = tk.Menu()
        self.style = style
        self.window = window
        self.Tree = {"name": "Menu", "children": [], "object": self.menu}

    def add(self):
        self.window.__add_child__(self)
        self.window.window.config(menu=self.menu)

    def __add_child__(self, child):
        self.Tree["children"].append(child)
        if child.submenu != None:
            self.menu.add_cascade(label=child.name, menu=child.submenu.menu)
        else:
            self.menu.add_command(label=child.name)

    def add_separator(self):
        self.menu.add_separator()


class SubMenu():
    def __init__(self, menu: Menu, name="SubMenu", submenu=None):
        self.name = name
        self.menu = menu
        self.submenu = submenu
        self.Tree = {"name": self.name, "children": [self.submenu], "object": self.submenu}

    def add(self):
        self.menu.__add_child__(self)
