import tkinter.messagebox
from tkinter import *


class CPI():
    def __init__(self):
        self.root = Tk()
        self.ent_1 = Entry(self.root)
        self.ent_2 = Entry(self.root)
        self.ent_3 = Entry(self.root)
        self.ent_4 = Entry(self.root)

        self.create_UI()

    def create_UI(self):
        # Create windows
        self.root.geometry("485x260")
        self.root.minsize(485, 250)
        self.root.maxsize(485, 250)
        # Create label
        lb_1 = Label(self.root, text="Principle Amount(Pa)")
        lb_2 = Label(self.root, text="Rate(%)")
        lb_3 = Label(self.root, text="Time(year)")
        lb_4 = Label(self.root, text="Compound Interest")
        # Config Entry
        self.ent_1.config(font=("Calibri", 25))
        self.ent_2.config(font=("Calibri", 25))
        self.ent_3.config(font=("Calibri", 25))
        self.ent_4.config(state="disable",font=("Calibri", 25), fg="green")
        # Create button
        btn_clr = Button(self.root, command= lambda : self.clear(), text="Clear", padx=50, pady=20, background="#356C99")
        btn_sbm = Button(self.root, command= lambda : self.calculator(), text="Submit", padx=150, pady=20, background="#94A61A")

        # Set grid
        # Row 1
        lb_1.grid(column=0, row=0)
        self.ent_1.grid(column=1, row=0)
        # Row 2
        lb_2.grid(column=0, row=1)
        self.ent_2.grid(column=1, row=1)

        # Row 3
        lb_3.grid(column=0, row=2)
        self.ent_3.grid(column=1, row=2)

        # Row 4
        btn_clr.grid(column=0, row=3)
        btn_sbm.grid(column=1, row=3)

        # Row 5
        lb_4.grid(column=0, row=4)
        self.ent_4.grid(column=1, row=4)

    def clear(self):
        text_1 = StringVar()
        text_2 = StringVar()
        text_3 = StringVar()
        text_4 = StringVar()
        text_1.set("")
        text_2.set("")
        text_3.set("")
        text_4.set("")
        self.ent_1.config(textvariable=text_1)
        self.ent_2.config(textvariable=text_2)
        self.ent_3.config(textvariable=text_3)
        self.ent_4.config(textvariable=text_4)

    def calculator(self):
        value_principle = self.ent_1.get()
        value_rate = self.ent_2.get()
        value_time = self.ent_3.get()
        if value_principle == "" or value_rate =="" or value_rate =="":
            tkinter.messagebox.showwarning(title="Miss some value", message="Please input all value!")
        elif not value_principle.isnumeric() or not value_rate.isnumeric() or not value_time.isnumeric():
            tkinter.messagebox.showwarning(title="Something wrong", message="Input must be Number!")
            self.clear()
        else:
            result = float(value_principle)
            value_rate = float(value_rate)
            value_time = float(value_time)
            while value_time > 1:
                result += result * value_rate / 100
                value_time -= 1
            result += result * value_rate / 100 * value_time

            text = StringVar()
            text.set(str(result))
            self.ent_4.config(textvariable=text)

    def run(self):
        root = self.root
        root.mainloop()


if __name__ == '__main__':

    x = "skdjhfg"
    cpi = CPI()
    cpi.run()
