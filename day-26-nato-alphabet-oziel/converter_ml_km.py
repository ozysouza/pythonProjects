from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=30, pady=30, background="white")

# Entry
miles_entry = Entry(width=5)
miles_entry.grid(row=3, column=4)

# Labels
miles_label = Label(text="Miles", background="white")
miles_label.grid(row=3, column=5)
miles_label.config(padx=5, pady=5)

km_label = Label(text="Km", background="white")
km_label.grid(row=4, column=5)
km_label.config(padx=5, pady=5)

equal_label = Label(text=" is equal to", background="white")
equal_label.grid(row=4, column=2)


# Button
def converter():
    miles = float(miles_entry.get())
    km = round(miles * 1.609, 4)
    converted_km.config(text=str(km))


calculate_bt = Button(text="Calculate", background="white", command=converter)
calculate_bt.grid(row=5, column=4)

converted_km = Label(text="", background="white")
converted_km.grid(row=4, column=4)

window.mainloop()
