from Tkinter import *
from tkFileDialog import askopenfilename
import Image , ImageTk


root = Tk()
root.geometry('500x500')

canvas = Canvas(root,width=350,height=350)
canvas.pack()

temp = None






#opens image on canvas
def opens():
    global img,idraw
    global tk_im
    filename = askopenfilename()
    im = Image.open(filename)
    tk_im = ImageTk.PhotoImage(im)              ## <------------
    a=canvas.create_image(200,200,anchor=CENTER,image=tk_im)
    idraw=ImageDraw.Draw(im)
    temp = filename




#open button
Openbutton = Button(root, text='Open',width =15, command=opens)
Openbutton.pack(side=BOTTOM, padx=2, pady=2)

#rotate button
rotatebutton = Button(root, text='Rotate',width =10)
rotatebutton.pack(side=BOTTOM, padx=2, pady=2)


#crop button
cropbutton = Button(root, text='Crop',width =10)
cropbutton.pack(side=BOTTOM, padx=2, pady=2)












mainloop()