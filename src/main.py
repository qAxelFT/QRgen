from email.mime import image
import tkinter
import qrcode
from tkinter import *
from tkinter import ttk
import os
from PIL import ImageTk, Image

save_path = "images/"
path, dirs, files = next(os.walk(f"{save_path}"))
file_count = len(files)

def gen():

        global file_count
        file_count = file_count + 1

        input_data = input_entry.get()

        qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)

        qr.add_data(input_data)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')
        img.save(f"{save_path}qr{file_count}.png")

        root.python_image = tkinter.PhotoImage(file=f"{save_path}qr{file_count}.png")
        ttk.Label(root, image=root.python_image).pack()

        

root = Tk()

input_entry = Entry(root, width=50)
input_entry.pack()

gen_button = Button(root, text="Gen", command=gen)
gen_button.pack()

root.mainloop()



