import tkinter

if __name__ == '__main__':
    window = tkinter.Tk()
    
    def calculate():
        price = int(price_per_item_entry.get())
        number = int(number_of_items_entry.get())
        total_price_entry.insert(0, string = str(price * number))
    
    price_per_item = tkinter.Label(window, text="Price per item")
    price_per_item_entry = tkinter.Entry(window)
    
    number_of_items = tkinter.Label(window, text="Number of items")
    number_of_items_entry = tkinter.Entry(window)
    
    total_price_label = tkinter.Label(window, text="Total price")
    total_price_entry = tkinter.Entry(window)
    
    calculate_button = tkinter.Button(window, text="Calculate",command=calculate)
    
    # grid works with rows and columns and is more flexible than place
    # like a matrix
    
    price_per_item.grid(row=0, column=0)
    price_per_item_entry.grid(row=0, column=1)
    number_of_items.grid(row=1, column=0)
    number_of_items_entry.grid(row=1, column=1)
    total_price_label.grid(row=2, column=0)
    total_price_entry.grid(row=2, column=1)
    calculate_button.grid(row=3, column=0, columnspan=2) 
    # colspan fit in 2 columns if 2
    # rowspan fit in 2 rows if 2
    
    window.mainloop()