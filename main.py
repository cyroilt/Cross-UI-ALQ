# устанавливаем путь к текущему каталогу
import sys
import os 
sys.path.append(os.getcwd())
from Widgets import Window,Button,Label,UI

#установка PIL через wheel в академии pip install --force-reinstall C:\путь_до_файла\pillow-10.4.0-cp38-cp38-win_amd64.whl
main = Window.Window(background=Window.LinearGradient(colors={0:(253,222,210,200),0.5:(100,230,12,100),1:(255,0,0,255)},size=(250,250),rotation=0))
main.__animation__player__.fps=144
mainMenu = Window.Menu(main)
fileSubMenu = Window.Menu(main)
minifs = Window.SubMenu(fileSubMenu,name="New")
minifs.add()
minifs = Window.SubMenu(fileSubMenu,name="Open")
minifs.add()
minifs = Window.SubMenu(fileSubMenu,name="Save")
minifs.add()
fileSubMenu.add_separator()
minifs = Window.SubMenu(fileSubMenu,name="Exit")
minifs.add()
mini = Window.SubMenu(mainMenu,name="File",submenu=fileSubMenu)
mini.add()
mini = Window.SubMenu(mainMenu,name="Edit")
mini.add()
mainMenu.add()
rotation=0
def button_click(event):
    global rotation
    print(event)
    event.widget.configure(background=Window.Color(size_of_area=(200,50),color=(100,100,100,200)))
    rotation+=4
    main.configure(background=Window.LinearGradient(colors={0:(253,222,210,200),0.5:(100,230,12,100),1:(255,0,0,255)},size=(250,250),rotation=rotation))
def button_unclick(event):
    print(event)
    event.widget.configure(background=Window.Color(size_of_area=(200,50),color=(100,100,0,200)))
uno_anim=0
duoanim=0
def onhovered(*args):
    uno_anim.play()
def onuhovered(*args):
    duoanim.play()
button = Button.Button(main, text="Click me",background=Window.Color(size_of_area=(200,50),color=(100,100,0,200)), size=(200, 50),position=(100,100))
uno_anim=UI.Animation(button,time=0.2,parameter_changing="background",from_state=Window.Color(size_of_area=(200,50),color=(100,100,0,200)),to_state=Window.Color(size_of_area=(200,50),color=(100,100,0,10)))
duoanim=UI.Animation(button,time=0.2,parameter_changing="background",to_state=Window.Color(size_of_area=(200,50),color=(100,100,0,200)),from_state=Window.Color(size_of_area=(200,50),color=(100,100,0,10)))
button.add()
button.bind("left-click",button_click)
button.bind("mouse-release",button_unclick)
button.bind("enter",onhovered)
button.bind("leave",onuhovered)
label=Label.Label(main,(100,300),foreground=Window.LinearGradient(colors={0:(0,222,210,200),0.5:(100,0,12,100),1:(255,255,255,255)},size=(50,20),rotation=0))
label.add()
main.window.mainloop()
