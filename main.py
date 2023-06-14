import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from interface import makecenter

root = Tk()
root.title("Chẩn đoán bệnh viêm quanh cuống")
root.resizable(height=False,width=False)
root.minsize(height=450,width=600)

frame = Frame(root)
frame.pack(side=BOTTOM,padx=15,pady=15)


def selectpic():
    filename = filedialog.askopenfilename(initialdir="E:\Study\TTM\Viêm quanh cuống goc",title="Select Image",filetypes=(("JPG File","*.jpg"),("PNG File","*.png")))
    img = Image.open(filename)
    img.thumbnail((200,200), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    lbl_show_pic.configure(image=img)
    lbl_show_pic.image = img


lbl_show_pic = Label(root)
lbl_show_pic.pack()

lbl_show_res_pic = Label(root)
lbl_show_res_pic.pack()

btn_browse = Button(frame, font=('verdana',16), text='Select Image', bg='grey', command=selectpic,width=11)
btn_browse.pack(side=tk.LEFT,padx=30)

btn_run = Button(frame, font=('verdana',16), text='Run', bg='grey', command=lambda :exit(),width=11)
btn_run.pack(side=tk.LEFT,padx=30)

makecenter(root)
root.mainloop()