from tkinter import *

window = Tk()
window.title('Miles - Kms Converter')
# window.minsize(width=300, height=150)
window.config(padx=20, pady=20)

input1 = Entry(width=8)
input1.grid(column=1, row=1)

miles = Label(text='Miles')
miles.grid(column=2, row=1)

equal = Label(text='is equal to')
equal.grid(column=0, row=2, sticky='E')

m = Label(text=0)
m.grid(column=1, row=2)

kilometer = Label(text='Kms')
kilometer.grid(column=2, row=2, sticky='W')


def cal():
    km = input1.get()
    res = float(km) * 1.6093
    m.config(text=round(res, 2))

calculate = Button(text='Calculate', command=cal)
calculate.grid(column=1, row=3)


window.mainloop()