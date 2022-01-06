from tkinter import *

from setuptools.command.rotate import rotate


def run():
    # Create new windows
    root = Tk()

    # Set size
    root.geometry("480x320")

    # Create menu
    menu = Menu()
    item = Menu()
    item.add_cascade(label='New')
    menu.add_cascade(label='File', menu=item)
    root.config(menu=menu)

    # Set tile
    root.title("First try Tkinter")

    # adding a label to the root window
    lbl = Label(root, text="Are you a Geek?")
    lbl.grid(column=0, row=0)

    # adding Entry Field+
    txt = Entry(root, width=20)
    txt.grid(column=1, row=0)

    # function to display user text when
    # button is clicked
    def clicked():
        res = "You wrote" + txt.get()
        lbl.configure(text=res)

    # button widget with red color text inside
    btn = Button(root, text="Click me", fg="red", command=clicked)
    # Set Button Grid
    btn.grid(column=2, row=0)


    root.mainloop()

if __name__ == '__main__':
    run()