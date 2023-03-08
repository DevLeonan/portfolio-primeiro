import tkinter as tk
from PIL import Image, ImageTk
import os

class SupermarketSystem:
    def __init__(self, root):
        self.root = root
        root.config(bg="#708090")
        self.root.title("Felpy_sistem")
        self.root.geometry("1200x700")

        label = tk.Label(root, text="Bem-vindo ao sistema Felpy_market")
        label.config(bg="#FF0000")
        label.pack(anchor="s")
        label.pack()

        image_path = os.path.abspath("image.jpg")
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)

        self.label = tk.Label(root, image=photo)
        self.label.pack()

        self.entry = tk.Entry(self.root)
        self.entry.pack()

        self.button = tk.Button(self.root, text="Add Item", command=self.add_item)
        self.button.pack()

    def add_item(self):
        item_name = self.entry.get()
        self.label.config(text="Item '{}' added to the cart".format(item_name))


root = tk.Tk()
app = SupermarketSystem(root)
root.mainloop()
