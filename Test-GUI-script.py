from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk

root = Tk()
root.geometry('100x50')

def open_file():
    file = askopenfilename(filetypes = [('PNG images', '*.png'), ('JPEG images', '*.jpg')])
    
    if file is not None:
        image = Image.open(file)
        wpercent = (400 / float(image.size[0]))
        hsize = int((float(image.size[1]) * float(wpercent)))
        image = image.resize((400, hsize), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        img = Label(image = photo)
        img.image = photo
        img.pack(side = TOP, pady = 20)
        root.geometry('{}x{}'.format(image.width + 100, image.height + 100))

btn = Button(root, text ='Open', command = lambda:open_file())
btn.pack(side = TOP, pady = 10)

mainloop()

# TODO: Logout button