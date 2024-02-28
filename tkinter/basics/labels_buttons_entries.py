import tkinter



if __name__ == '__main__':
    window = tkinter.Tk()
    window.title("Tkinter basics")
    window.geometry('600x400')
    
    def printHandler():
        print(textentry.get())
    
    label = tkinter.Label(window, text='Hello world.', bg='blue', fg='white', width=30)
    label.pack()
    
    # textentry can be used to get the input from the user
    textentry = tkinter.Entry(window, bg='green', fg='white', width=30, show='*')
    textentry.pack()
    
    button = tkinter.Button(window, text = "Click me", bg='violet', activebackground='green',activeforeground='white',state=tkinter.DISABLED) 
    #activebackground and activeforeground are used to change the color of the button when it is clicked
    button.pack()
    
    button2 = tkinter.Button(window, text='print hello world', command=printHandler)
    button2.pack()
    
    window.mainloop()