import tkinter.messagebox
from tkinter import *


def check_number(number):
    try:
        float(number)
        return True
    except:
        return False


class LoanCalculator():
    def __init__(self):
        self.root = Tk()

        self.lb_month_pay = Label(self.root, font=("Calibri", 25))
        self.lb_total_pay = Label(self.root, font=("Calibri", 25))
        # Create entry to input value
        self.entry_annual = Entry(self.root, font=("Calibri", 25), justify=RIGHT)
        self.entry_year = Entry(self.root, font=("Calibri", 25), justify=RIGHT)
        self.entry_loan = Entry(self.root, font=("Calibri", 25), justify=RIGHT)

        self.createUI()

    def createUI(self):
        # Set size
        self.root.geometry("460x300")
        self.root.minsize(460, 300)
        self.root.maxsize(460, 300)
        # Create Label
        lb_annual = Label(self.root, text="Annual Interest Rate")
        lb_year = Label(self.root, text="Number of Years")
        lb_loan = Label(self.root, text="Loan Amount")
        lb_month = Label(self.root, text="Monthly Payment")
        lb_total = Label(self.root, text="Total Payment")
        # Create button compute payment
        btn = Button(self.root, command=lambda: self.compute(), text="Compute Payment", padx=150, pady=20,
                     background="#94A61A")

        # Set location
        # Row 1
        lb_annual.grid(column=0, row=0)
        self.entry_annual.grid(column=1, row=0)
        # Row 2
        lb_year.grid(column=0, row=1)
        self.entry_year.grid(column=1, row=1)
        # Row 3
        lb_loan.grid(column=0, row=2)
        self.entry_loan.grid(column=1, row=2)
        # Row 4
        lb_month.grid(column=0, row=3)
        self.lb_month_pay.grid(column=1, row=3)
        # Row 5
        lb_total.grid(column=0, row=4)
        self.lb_total_pay.grid(column=1, row=4)
        # Row 6
        btn.grid(column=0, row=5, columnspan=2)

    def clear(self):
        text_1 = StringVar()
        text_2 = StringVar()
        text_3 = StringVar()
        text_1.set("")
        text_2.set("")
        text_3.set("")
        self.entry_annual.config(textvariable=text_1)
        self.entry_year.config(textvariable=text_2)
        self.entry_loan.config(textvariable=text_3)
        self.lb_month_pay.config(text="")
        self.lb_total_pay.config(text="")

    def compute(self):
        rate = self.entry_annual.get()
        year = self.entry_year.get()
        loan = self.entry_loan.get()

        if rate == "" or year == "" or loan == "":
            tkinter.messagebox.showwarning(title="Miss some value", message="Please input all value!")
        elif not check_number(rate) or not check_number(year) or not check_number(loan):
            tkinter.messagebox.showwarning(title="Something wrong", message="Please input number!")
            self.clear()
        else:
            rate = float(rate) / 1200
            year = float(year)
            loan = float(loan)
            total_month = year * 12

            month_pay = loan * rate / (1 - 1 / (1 + rate) ** total_month)
            total_pay = month_pay * 12 * year
            self.lb_month_pay.config(text=format(month_pay, '10.2f'))
            self.lb_total_pay.config(text=format(total_pay, '10.2f'))

    def run(self):
        root = self.root
        root.mainloop()


if __name__ == '__main__':
    loan = LoanCalculator()
    loan.run()
