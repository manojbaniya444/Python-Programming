import tkinter
from tkinter import messagebox

if __name__  == '__main__':
    window = tkinter.Tk()
    
    def showInfo():
        messagebox.showinfo(title='Info', message='Hello World')
        
    def showError():
        messagebox.showerror(title='Error', message='Hello World')
        
    def showWarning():
        messagebox.showwarning(title='Warning', message='Hello World')
        
    def askQuestion():
        result1 = messagebox.askquestion(title='Question', message='Do you wish to proceed?')
        # print(result1) # yes/no
        result2 = messagebox.askyesno(title='Question', message='Do you wish to proceed?')
        # print(result2) # True/False

        
        if result1 == "Yes" and result2 == True:
            print('You chose to proceed')
        else:
            print('You chose not to proceed')
    
    def askretrycancel():
        result = messagebox.askretrycancel(title='Retry', message='Do you wish to retry?')
        if result == True:
            print('You chose to retry')
        else:
            print('You chose not to retry')
            
    def askokcancel():
        result = messagebox.askokcancel(title='Ok', message='Do you wish to proceed?')
        if result == True:
            print('You chose to proceed')
        else:
            print('You chose not to proceed')
        
    
    button = tkinter.Button(window, text="Click me", command=showInfo)
    button.pack()
    
    
    window.mainloop()