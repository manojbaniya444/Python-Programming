import tkinter

def hello():
    print("Hello world.")

if __name__ == '__main__':
    window = tkinter.Tk()
    # name for the window title
    window.title("My first tkinter app.")
    
    # set the size of the window
    window.geometry('600x400')
    
    # frame is a container and contains labels and buttons
    # frame is inside the window
    # window > frame > label, button
    # nesting is possible
    frame = tkinter.Frame(window)
    frame.pack()
    
    # ?widgets
    # *window is the parent of the label and button
    label = tkinter.Label(frame, text="Hello world.")
    button = tkinter.Button(frame, text="Hello world.", command=hello)
    
    # ?geometry manager
    # *label is instance of Label class
    # *pack places the label in the window (container)
    # *There are other geometry managers like grid and place
    label.pack()
    button.pack()
    
    
    # this loop will keep on running the window handling the events
    window.mainloop()
    # This will run only when the window is closed because the mainloop blocks the code below it.
    # print("Hello world.")