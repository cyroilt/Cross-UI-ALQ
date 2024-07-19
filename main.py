from Widgets import Window,Button
#установка PIL через wheel в академии pip install --force-reinstall C:\путь_до_файла\pillow-10.4.0-cp38-cp38-win_amd64.whl
main = Window.Window(background=Window.RadialGradient(colors={0:(253,222,210,200),0.5:(100,230,12,100),1:(255,0,0,255)},size=(250,250),rotation=0))
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

button = Button.Button(main, text="Click me",background=Window.Color(size_of_area=(200,50),color=(100,100,0,200)), size=(200, 50))

button.add()
main.window.mainloop()
