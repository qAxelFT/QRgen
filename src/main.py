from email.mime import image
import tkinter
import qrcode
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

def gen():
        
        input_data = input_entry.get()

        qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)

        qr.add_data(input_data)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')
        img.save("images/qr.png")

        root.python_image = tkinter.PhotoImage(file='images/qr.png')
        ttk.Label(root, image=root.python_image).pack()
        

root = Tk()

input_entry = Entry(root, width=50)
input_entry.pack()

gen_button = Button(root, text="Gen", command=gen)
gen_button.pack()

root.mainloop()



