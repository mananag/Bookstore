from tkinter import *

from backend import *


def get_selected_row(e):
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    e1.delete(0, END)
    e1.insert(END, selected_tuple[1])
    e2.delete(0, END)
    e2.insert(END, selected_tuple[2])
    e3.delete(0, END)
    e3.insert(END, selected_tuple[3])
    e4.delete(0, END)
    e4.insert(END, selected_tuple[4])


def view_command():
    list1.delete(0, END)
    for row in view():
        list1.insert(END, row)


def search_command():
    list1.delete(0, END)
    for row in search("%" + e1.get() + "%", "%" + e2.get() + "%",
                      "%" + e3.get() + "%", "%" + e4.get() + "%"):
        list1.insert(END, row)


def add_command():
    check = search("%" + e1.get() + "%", "%" + e2.get() + "%",
                   "%" + e3.get() + "%", "%" + e4.get() + "%")
    if len(check) == 0:
        insert(e1.get(), e2.get(), e3.get(), e4.get())
        search_command()
    else:
        list1.delete(0, END)
        list1.insert(END, "Sorry book already existed")


def delete_command():
    delete(selected_tuple[0])
    view_command()


def update_command():
    update(selected_tuple[0], e1.get(), e2.get(), e3.get(), e4.get())
    view_command()


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

list1.bind('<<ListboxSelect>>', get_selected_row)

# Buttons
b1 = Button(window, text="View All", width=12, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search Entry", width=12, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add Entry", width=12, command=add_command)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update", width=12, command=update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.title("Bookstore")

window.mainloop()
