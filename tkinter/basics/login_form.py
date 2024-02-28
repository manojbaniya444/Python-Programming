import tkinter
from tkinter import messagebox
import sqlite3

if __name__ == '__main__':
    window = tkinter.Tk()
    window.title("Login Form")
    window.geometry('400x400')
    window.configure(bg='#333333') # dark grey window background
    
    # frame is a tkinter container
    frame = tkinter.Frame(bg='#333333')
    
    def login():
        password = 'test'
        
        username_entry_value = username_entry.get()
        password_entry_value = password_entry.get()
        
        if password_entry_value == password:
            print('Login successful')
            messagebox.showinfo(title='Login info',message="You logged in successfully")
            
            # save the username and password to a sqlite database
            
            # connection
            # if the database does not exist, it will be created
            connect_db = sqlite3.connect('login.db')
            table_create_query = '''CREATE TABLE IF NOT EXISTS Login_Data
            (
                username TEXT,
                password Text
            )
            '''
            
            connect_db.execute(table_create_query)
            
            # insert into database
            insert_query = '''
            INSERT INTO Login_Data (username, password)
            VALUES (?, ?)
            '''
            
            insert_data_tuple = (username_entry_value, password_entry_value)
            
            cursor = connect_db.cursor()
            cursor.execute(insert_query, insert_data_tuple)
            connect_db.commit()
            
            connect_db.close()
        else:
            print("Invalid login")
            messagebox.showerror(title='Login info',message="Invalid login")
    
    login_label = tkinter.Label(frame, text='Login',bg='#333333',fg='white',font=('Arial', 30))
    username_label = tkinter.Label(frame, text='Username',bg='#333333',fg='white',font=('Arial', 20))
    username_entry = tkinter.Entry(frame,font=('Arial', 20))
    password_label = tkinter.Label(frame, text='Password',bg='#333333' ,fg='white',font=('Arial', 20))
    password_entry = tkinter.Entry(frame, show='*',font=('Arial',20))
    login_button = tkinter.Button(frame, text="Login",bg='#ff3399',fg='white',font=('Arial', 20), command=login)

    # placing the widgets on the screen
    login_label.grid(row=0, column=0, columnspan=2, sticky='news',pady=40) # take up space in all 4 directions
    username_label.grid(row=1, column=0)
    username_entry.grid(row=1, column=1,pady=20)
    password_label.grid(row=2, column=0)
    password_entry.grid(row=2, column=1,pady=20)
    login_button.grid(row=3, column=0, columnspan=2,pady=30)
    
    
    # place the frame
    frame.pack()
    
    
    
    window.mainloop()