from tkinter import *


class UI():
    def __init__(self):
        self.root = Tk()
        self.flag_eq = False
        # Element
        self.self_element_math = ['+', '-', '*', '/']
        # Box screen
        equal = StringVar()
        equal.set('0')
        self.screen_box = Entry(self.root, textvariable=equal, font=("Calibri", 25),fg="white")

        # Add button
        self.btn_1 = Button(self.root, command=lambda: self.click_button('1'), text="1", height=2, width=10, bg="#424548", fg="white")
        self.btn_2 = Button(self.root, command=lambda: self.click_button('2'), text="2", height=2, width=10, bg="#424548", fg="white")
        self.btn_3 = Button(self.root, command=lambda: self.click_button('3'), text="3", height=2, width=10, bg="#424548", fg="white")
        self.btn_4 = Button(self.root, command=lambda: self.click_button('4'), text="4", height=2, width=10, bg="#424548", fg="white")
        self.btn_5 = Button(self.root, command=lambda: self.click_button('5'), text="5", height=2, width=10, bg="#424548", fg="white")
        self.btn_6 = Button(self.root, command=lambda: self.click_button('6'), text="6", height=2, width=10, bg="#424548", fg="white")
        self.btn_7 = Button(self.root, command=lambda: self.click_button('7'), text="7", height=2, width=10, bg="#424548", fg="white")
        self.btn_8 = Button(self.root, command=lambda: self.click_button('8'), text="8", height=2, width=10, bg="#424548", fg="white")
        self.btn_9 = Button(self.root, command=lambda: self.click_button('9'), text="9", height=2, width=10, bg="#424548", fg="white")
        self.btn_plush = Button(self.root, command=lambda: self.click_button('+'), text="+", height=2, width=10, bg="#70757A", fg="white")
        self.btn_minus = Button(self.root, command=lambda: self.click_button('-'), text="-", height=2, width=10, bg="#70757A", fg="white")
        self.btn_time = Button(self.root, command=lambda: self.click_button('*'), text="x", height=2, width=10, bg="#70757A", fg="white")
        self.btn_div = Button(self.root, command=lambda: self.click_button('/'), text="/", height=2, width=10, bg="#70757A", fg="white")
        self.btn_dot = Button(self.root, command=lambda: self.click_button('.'), text=".", height=2, width=10, bg="#424548", fg="white")
        self.btn_clr = Button(self.root, command=lambda: self.clear(), text="clear", height=2, width=10, fg="#E73121")
        self.btn_eq = Button(self.root, command=lambda: self.calculator_value(), text="=", height=2, width=10, bg="#AECBFA", fg="white")

        self.set_location()

    def clear(self):
        text = StringVar()
        text.set("0")
        self.screen_box.config(textvariable=text)

    def do_time_div(self, list_calculator):
        while True:
            idx_time = list_calculator.index("*") if "*" in list_calculator else 9999999999
            idx_div = list_calculator.index("/") if "/" in list_calculator else 9999999999
            if idx_time == idx_div:
                break
            elif idx_time < idx_div:
                flag_math = True
                idx_temp = idx_time
            else:
                flag_math = False
                idx_temp = idx_div
            if idx_temp == 0:
                return []
            elif list_calculator[idx_temp - 1] == "" or list_calculator[idx_temp + 1] == "":
                return []
            else:
                if flag_math:
                    list_calculator[idx_temp - 1] = str(
                        float(list_calculator[idx_temp - 1]) * float(list_calculator[idx_temp + 1]))
                else:
                    list_calculator[idx_temp - 1] = str(
                        float(list_calculator[idx_temp - 1]) / float(list_calculator[idx_temp + 1]))
                list_calculator.pop(idx_temp)
                list_calculator.pop(idx_temp)
        return list_calculator

    def do_plus_minus(self, list_calculator):
        while len(list_calculator) > 1:
            temp = list_calculator[1]
            if temp != "+" and temp != "-":
                return []
            else:
                if list_calculator[0] == "" or list_calculator[2] == "":
                    return []
                else:
                    if temp == "+":
                        list_calculator[0] = str(float(list_calculator[0]) + float(list_calculator[2]))
                    else:
                        list_calculator[0] = str(float(list_calculator[0]) - float(list_calculator[2]))
                    list_calculator.pop(1)
                    list_calculator.pop(1)
        return list_calculator

    def calculator_value(self):
        text = self.screen_box.get()
        if text == "ERROR" or text == "":
            self.set_screen_box("0")
            return
        list_value = text.split(" ")
        if list_value[-1] == '':
            list_value = list_value[:-2]
        print(list_value)
        # Do time first
        list_value = self.do_plus_minus(self.do_time_div(list_value)) if '' not in list_value else []
        if len(list_value) == 0:
            self.set_screen_box("ERROR")
        else:
            temp_1 = float(list_value[0])
            temp_2 = int(float(list_value[0]))
            if temp_1 - temp_2 == 0:
                self.set_screen_box(temp_2)
            else:
                self.set_screen_box(temp_1)
            self.flag_eq = True

    def set_screen_box(self, text):
        text_string_var = StringVar()
        text_string_var.set(str(text))
        self.screen_box.config(textvariable=text_string_var)

    def click_button(self, btn_text):
        text = self.screen_box.get()
        if text == "ERROR" or text == "0":
            text = ""
        if self.flag_eq:
            self.flag_eq = False
            if btn_text not in self.self_element_math:
                text = ""
        if btn_text in self.self_element_math:
            text += " " + str(btn_text) + " "
        else:
            text += str(btn_text)
        self.set_screen_box(text)

    def set_location(self):
        # Set size
        self.root.geometry("345x200")
        self.root.minsize(345, 215)
        self.root.maxsize(345, 215)

        # Set title
        self.root.title("Calculator")

        # Add screen show number, equal
        self.screen_box.grid(column=0, row=0, columnspan=4)
        # screen_box.pack()
        self.screen_box.config(state="disable", background="#FFFFFF")

        # Row 1 ======================================
        self.btn_7.grid(column=0, row=1)
        self.btn_8.grid(column=1, row=1)
        self.btn_9.grid(column=2, row=1)
        self.btn_plush.grid(column=3, row=1)
        # Row 2 ==========================
        self.btn_4.grid(column=0, row=2)
        self.btn_5.grid(column=1, row=2)
        self.btn_6.grid(column=2, row=2)
        self.btn_minus.grid(column=3, row=2)
        # Row 3 ========================
        self.btn_1.grid(column=0, row=3)
        self.btn_2.grid(column=1, row=3)
        self.btn_3.grid(column=2, row=3)
        self.btn_time.grid(column=3, row=3)

        # Row 4===========================
        self.btn_dot.grid(column=0, row=4)
        self.btn_clr.grid(column=1, row=4)
        self.btn_eq.grid(column=2, row=4)
        self.btn_div.grid(column=3, row=4)

    def run(self):
        root = self.root
        while True:
            root.mainloop()


if __name__ == '__main__':
    ui = UI()
    ui.run()
