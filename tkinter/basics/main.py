import tkinter as tk

window = tk.Tk()

def hello():
    print("Hello world.")

# when i click the hello button, it will run the hello function
button = tk.Button(window, text='Hello world', command=hello)
# ppack the button in the interface
button.pack()

# this will run the window in a loop
window.mainloop()