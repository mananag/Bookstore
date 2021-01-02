from tkinter import *
import backend

window = Tk()

# Title Label
l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

# Title Entry
e1 = Entry(window)
e1.grid(row=0, column=1)

# Author Label
l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

# Author Entry
e2 = Entry(window)
e2.grid(row=0, column=3)

# Year Label
l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

# Year Entry
e3 = Entry(window)
e3.grid(row=1, column=1)

# ISBN Label
l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

# ISBN Entry
e4 = Entry(window)
e4.grid(row=1, column=3)

# List Box
list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

# Scrollbar
sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

# Buttons
b1 = Button(window, text="View All", width=12)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search Entry", width=12)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add Entry", width=12)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update", width=12)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete", width=12)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12)
b6.grid(row=7, column=3)

window.title("Bookstore")

window.mainloop()
