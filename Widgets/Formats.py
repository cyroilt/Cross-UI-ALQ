import tkinter as tk

from PIL import Image as im
from PIL import ImageTk as imtk
import numba
from PIL import ImageFont
from PIL import ImageDraw as imgdw
import numpy as np
class Color():
    def __init__(self, size_of_area=(0, 0), color=(0, 0, 0, 0)):
        self.__color__=color
        self.size=size_of_area
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
#@numba.jit(fastmath=True,cache=True,parallel=True)
def fast_render_radial(height, width,rotation,sorted_points,color_points,gradient,center):
        max_dist = np.sqrt(center[0]**2 + center[1]**2)
        # Precompute trigonometric values
        y, x = np.ogrid[:height, :width]
        x = x - center[0]
        y = y - center[1]

        # Calculate the distance from the center
        dist = np.sqrt(x**2 + y**2) / max_dist

        # Initialize the gradient array
        

        # Interpolate colors
        for i in range(len(sorted_points) - 1):
            p1, p2 = sorted_points[i], sorted_points[i + 1]
            c1, c2 = color_points[p1], color_points[p2]
            
            mask = (dist >= p1) & (dist <= p2)
            t = (dist[mask] - p1) / (p2 - p1)
            
            gradient[mask, 0] = (c1[0] + t * (c2[0] - c1[0])).astype(np.uint8)
            gradient[mask, 1] = (c1[1] + t * (c2[1] - c1[1])).astype(np.uint8)
            gradient[mask, 2] = (c1[2] + t * (c2[2] - c1[2])).astype(np.uint8)
            gradient[mask, 3] = (c1[3] + t * (c2[3] - c1[3])).astype(np.uint8)
        return gradient
#@numba.jit(fastmath=True,cache=True,parallel=True)
def fast_render(height, width,rotation,sorted_points,color_points,pixels):
    
    # Precompute trigonometric values
        cos_theta = np.cos(np.radians(rotation))
        sin_theta = np.sin(np.radians(rotation))
        
        # Create a meshgrid for pixel coordinates
        x, y = np.meshgrid(numba.prange(width), numba.prange(height))
        
        # Calculate the position along the gradient for each pixel
        pos = (x / width) * cos_theta + (y / height) * sin_theta
        
        # Sort the color points
        sorted_points = sorted(color_points.keys())
        
        # Create arrays for interpolation
        p1 = np.zeros_like(pos)
        p2 = np.zeros_like(pos)
        c1 = np.zeros((height, width, 4), dtype=int)
        c2 = np.zeros((height, width, 4), dtype=int)
        
        # Find the two closest points for each position
        for i in numba.prange(len(sorted_points) - 1):
            mask = (sorted_points[i] <= pos) & (pos <= sorted_points[i + 1])
            p1[mask] = sorted_points[i]
            p2[mask] = sorted_points[i + 1]
            c1[mask] = color_points[sorted_points[i]]
            c2[mask] = color_points[sorted_points[i + 1]]
        
        # Interpolate between the two closest points
        t = (pos - p1) / (p2 - p1)
        t = np.clip(t, 0, 1)  # Ensure t is within [0, 1]
        
        r = (c1[..., 0] + t * (c2[..., 0] - c1[..., 0])).astype(int)
        g = (c1[..., 1] + t * (c2[..., 1] - c1[..., 1])).astype(int)
        b = (c1[..., 2] + t * (c2[..., 2] - c1[..., 2])).astype(int)
        a = (c1[..., 3] + t * (c2[..., 3] - c1[..., 3])).astype(int)
        
        # Set the pixel colors
        pixels[..., 0] = r
        pixels[..., 1] = g
        pixels[..., 2] = b
        pixels[..., 3] = a
        return pixels  
class LinearGradient():

    
    def __init__(self, colors={0:(0,0,0,255),100:(255,255,255,255)},size=(300,300),rotation=0):
        self.size=size
        self.rotation=rotation
        self.width=size[0]
        self.height=size[1]
        self.color_points=colors
        self.sorted_points = sorted(self.color_points.keys())
        self.img = im.new("RGBA", (self.width, self.height))
        self.pixels = np.zeros((self.height, self.width, 4), dtype=np.uint8)

        # Create an image from the array
        self.img = im.fromarray(fast_render(self.height,self.width,self.rotation,self.sorted_points,self.color_points,self.pixels), "RGBA")
    def add_to_canvas(self):
        self.upper=imtk.PhotoImage(self.img)
        return self.upper
class RadialGradient():
    def __init__(self, colors={0:(0,0,0,255),100:(255,255,255,255)},size=(300,300),rotation=0,center=(150,150)):
        self.size=size
        self.rotation=rotation
        self.center=center
        self.width=size[0]
        self.height=size[1]
        self.color_points=colors
        self.sorted_points = sorted(self.color_points.keys())
        self.img = im.new("RGBA", (self.width, self.height))
        self.pixels = np.array(self.img)
        # Create an image from the array
        self.img = im.fromarray(fast_render_radial(self.height,self.width,self.rotation,self.sorted_points,self.color_points,self.pixels,self.center), "RGBA")
    def add_to_canvas(self):
        self.upper=imtk.PhotoImage(self.img)
        return self.upper       

class Foreground():
    def __init__(self, text=None, maker=None, for_object=None,font=("arial",20)):
        self.text = text
        self.alphamask = maker
        self.objectTo = for_object
        self.fontn=f"{font[0]}.ttf"
        self.font=ImageFont.truetype(self.fontn,float(font[1]))
        if self.text != None:
            if type(self.objectTo) == Color:

                self.text_img = im.new("L", self.objectTo.color.size, 0)
                self.test_img_draw=imgdw.Draw(self.text_img)
                self.txtsz = self.test_img_draw.textbbox((0,0),self.text,font=self.font)
                self.test_img_draw.text(((self.objectTo.color.size[0]-self.txtsz[2])/2,(self.objectTo.color.size[1]-self.txtsz[3])/2),self.text,fill=255,font=self.font)
                self.new_object = self.objectTo.color.copy()
                self.new_object.putalpha(self.text_img)

                print(self.new_object)
            elif type(self.objectTo) == LinearGradient or type(self.objectTo) == RadialGradient:
                self.text_img = im.new("L", self.objectTo.img.size, 0)
                self.test_img_draw = imgdw.Draw(self.text_img)
                self.txtsz=self.test_img_draw.textbbox((0,0),self.text,font=self.font)
                self.test_img_draw.text(((self.objectTo.img.size[0]-self.txtsz[2])/2,(self.objectTo.img.size[1]-self.txtsz[3])/2), self.text, fill=255,font=self.font)
                self.new_object = self.objectTo.img.copy()
                self.new_object.putalpha(self.text_img)
        else:
            pass
    def add_to_canvas(self):
        self.upper = imtk.PhotoImage(self.new_object)
        return self.upper