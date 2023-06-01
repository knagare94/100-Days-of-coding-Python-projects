from tkinter import *


def miles_to_km():
    miles = float(mile_input.get())
    km = round(miles * 1.609)
    km_result_label.config(text=f"{km}")

windows = Tk()
windows.title("Mile to Km Converter")
windows.config(padx=20, pady=20)

is_equal_label = Label(text="is equal to", font=("Arial", 10, "bold"))
is_equal_label.grid(column=0, row=1)

mile_input = Entry(width=10)
mile_input.grid(column=1, row=0)

miles_label = Label(text="Miles", font=("Arial", 10, "bold"))
miles_label.grid(column=2, row=0)

km_label = Label(text="KM", font=("Arial", 10, "bold"))
km_label.grid(column=2, row=1)

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=3)


windows.mainloop()
