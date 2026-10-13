import os
from PIL import Image, ImageTk

def charger_image(path, size=None):
    pil_image = Image.open(path)

    if size:
        pil_image = pil_image.resize(size)

    return ImageTk.PhotoImage(pil_image)

def clear_root(root):
    for widget in root.winfo_children():
        widget.destroy()

