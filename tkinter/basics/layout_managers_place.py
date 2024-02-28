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
    
    
    # place works with absolute positioning
    # price_per_item.place(x=10, y=10)
    # price_per_item_entry.place(x=100, y=10)

    widgets = [price_per_item, price_per_item_entry, number_of_items, number_of_items_entry, total_price_label, total_price_entry, calculate_button]
    
    for i in range(len(widgets)):
        # x will be 10, y will be 10 + i * 30 y will be different for all items.
        widgets[i].place(x=10, y=10 + i * 30)
    
    window.mainloop()