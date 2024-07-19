import tkinter as tk

from PIL import Image as im
from PIL import ImageTk as imtk


class Color():
    def __init__(self, size_of_area=(0, 0), color=(0, 0, 0, 0)):
        self.__color__=color
        self.color = im.new("RGBA", size=size_of_area, color=color)

    def add_to_canvas(self):
        self.upper = imtk.PhotoImage(self.color)
        return self.upper


class Image():
    def __init__(self, path):
        self.image = im.open(path)

    def add_to_canvas(self):
        return imtk.PhotoImage(self.image)


class GIFAnimation():
    def __init__(self, path, preload=True):
        self.preload = Image.open(path)
        self.frames_count = self.preload.n_frames
        self.frames = []
        self.preload = preload
        self.loop = 0
        self.path = path
        if preload:
            for i in range(self.frames_count):
                self.frames.append(tk.PhotoImage(file=path, format=f"gif -index {i}"))

    def animate(self, partofanim, current_frame=0):
        if current_frame == self.frames_count:
            current_frame = 0
        if self.preload:
            partofanim.configure(image=current_frame)
        else:
            partofanim.configure(image=tk.PhotoImage(file=self.path, format=f"gif -index {current_frame}"))
        current_frame += 1
        self.loop = partofanim.after(50, lambda: self.animate(partofanim, current_frame=current_frame))

    def stop_animation(self, partofanim):
        partofanim.after_cancel(self.loop)
