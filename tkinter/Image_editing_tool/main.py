import tkinter
from tkinter import filedialog
from tkinter import colorchooser
from PIL import Image, ImageOps, ImageTk, ImageFilter
from tkinter import ttk

root = tkinter.Tk()
root.geometry('1000x600')
root.title("Image Editing App")
root.config(bg='white')

pen_color = 'black'
pen_size = 5
file_path = ''

def clear_canvas():
    canvas.delete('all')
    canvas.create_image(0,0,image=canvas.image,anchor='nw')

def change_size(size):
    global pen_size
    pen_size = size

def change_color():
    global pen_color
    pen_color = colorchooser.askcolor(title="Pick a color")[1]
    
def draw(event):
    x1, y1 = (event.x - pen_size), (event.y - pen_size)
    x2, y2 = (event.x + pen_size), (event.y + pen_size)
    canvas.create_oval(x1, y1, x2, y2, fill=pen_color, outline='')

def add_image():
    global file_path
    file_path = filedialog.askopenfilename(initialdir='D:\Learn Python\tkinter\Image_editing_tool\images')
    image = Image.open(file_path)
    # width, height = int(image.width/2), int(image.height/2)
    width, height = 750,550
    image = image.resize((width, height), Image.LANCZOS )
    # set the size of the canvas to the size of the image
    canvas.config(width=image.width, height=image.height)
    # create a new image object to work with
    image = ImageTk.PhotoImage(image)
    canvas.image = image
    canvas.create_image(0, 0, image=image, anchor='nw')
    
def apply_filter(filtername):
    # need to re-open the image because we cannot use tkinter image object with PIL
    image = Image.open(file_path)
    image = image.resize((750,550), Image.LANCZOS)
    
    if filtername == "Black and White":
        image = ImageOps.grayscale(image)
    elif filtername == "Blur":
        image = image.filter(ImageFilter.BLUR)
    elif filtername == "Emboss":
        image = image.filter(ImageFilter.EMBOSS)
    elif filtername == "Sharpen":
        image = image.filter(ImageFilter.SHARPEN)
    elif filtername == "Smooth":
        image = image.filter(ImageFilter.SMOOTH)
        
    image = ImageTk.PhotoImage(image)
    canvas.image = image
    canvas.create_image(0, 0, image=image, anchor='nw')
    
left_frame = tkinter.Frame(root, width=200, height=600, bg='white')
left_frame.pack(side='left',fill="both")

# ?Create canvas
canvas = tkinter.Canvas(root, width=750,height=550)
canvas.pack(pady=15)

# ?Choose image to show

image_button = tkinter.Button(left_frame, text="Add Image", bg='white', command=add_image)
image_button.pack(pady=15)

# ?Color change

color_button = tkinter.Button(left_frame, text="Change Color", bg='white', command=change_color)
color_button.pack(pady=15)

# ?Pen size

pen_size_frame = tkinter.Frame(left_frame, bg='white')
pen_size_frame.pack(pady=15)

pen_size1 = tkinter.Radiobutton(pen_size_frame,text='Small', value=3, bg='white', command=lambda: change_size(3)) # lambda required if you want to pass a value to the function
pen_size1.pack(side='left')

pen_size2 = tkinter.Radiobutton(pen_size_frame,text='Medium', value=5, bg='white', command=lambda: change_size(5))
pen_size2.pack(side='left')
pen_size2.select()

pen_size3 = tkinter.Radiobutton(pen_size_frame,text='Large', value=7, bg='white',command=lambda: change_size(7))
pen_size3.pack(side='left')

# ?clear button
clear_button = tkinter.Button(left_frame, text="Clear",command=clear_canvas, bg='white')
clear_button.pack(pady=15)

# ?combobox
filter_label = tkinter.Label(left_frame, text="Select Filter", bg='white')
filter_label.pack(pady=15)

filter_combobox = ttk.Combobox(left_frame, values=["Black and White","Blur","Emboss","Sharpen","Smooth"])
filter_combobox.pack()

# *binding the combobox to a function
filter_combobox.bind("<<ComboboxSelected>>", lambda e: apply_filter(filter_combobox.get()))

# ?draw on canvas
canvas.bind("<B1-Motion>", draw)


root.mainloop()