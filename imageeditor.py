from Tkinter import *
from tkFileDialog import askopenfilename
import Image , ImageTk


root = Tk()
root.geometry('500x500')
tk_im=None


canvas = Canvas(root,width=200,height=300)
canvas.pack()

def opens():
    global img,idraw
    global tk_im
    filename = askopenfilename()
    im = Image.open(filename)
    tk_im = ImageTk.PhotoImage(im)              ## <------------
    a=canvas.create_image(0,0,image=tk_im)
    idraw=ImageDraw.Draw(im)




#open button
Openbutton = Button(root, text='Open',width =15, command=opens)
Openbutton.pack(side=TOP, padx=2, pady=2)










mainloop()