import tkinter

if __name__ == '__main__':
    window = tkinter.Tk()
    
    def calculate():
        price = float(price_per_item_entry.get())
        number = float(number_of_items_entry.get())
        total_price_entry.insert(0, string = str(price * number))
    
    price_per_item = tkinter.Label(window, text="Price per item")
    price_per_item_entry = tkinter.Entry(window)
    
    number_of_items = tkinter.Label(window, text="Number of items")
    number_of_items_entry = tkinter.Entry(window)
    
    total_price_label = tkinter.Label(window, text="Total price")
    total_price_entry = tkinter.Entry(window)
    
    calculate_button = tkinter.Button(window, text="Calculate",command=calculate)
    
    price_per_item.pack()
    price_per_item_entry.pack()
    number_of_items.pack()
    number_of_items_entry.pack()
    total_price_label.pack(side='left') # comes side by side this will be on left
    total_price_entry.pack(side='right') # this will be on the right side
    # calculate_button.pack(fill='x') # fill the x axis by button
    
    window.mainloop()