import tkinter as tk
from Operations import *


class Calculator:

    __BUTTON_HEIGHT = 2
    __BUTTON_WIDTH = 5
    __OPERATION = ""
    __OPERATION_SYMBOLS = ["+", "-", "*", "/", "="]
    __NUMBER1 = 0
    __NUMBER2 = 0

    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.winfo_toplevel().title('Calculator')
        self.main_window.resizable(0, 0)

        background = tk.Frame(master=self.main_window)

        self.__add_text_box(self.main_window)
        self.__add_numbers_buttons(background)
        self.__add_positive_negative_buttons(background)
        self.__add_operation_buttons(background)
        self.__add_dot_button(background)
        self.__add_clear_buttons(background)

        background.pack()

    def __add_text_box(self, text_box_master):
        self.__entry_text = tk.StringVar()
        self.__text_box = tk.Entry(master=text_box_master, bg='white', width=20, justify='right', textvariable=self.__entry_text, state=tk.DISABLED)
        self.__text_box["font"] = ("Arial", 14, "bold")
        self.__text_box["disabledforeground"] = 'black'
        self.__text_box["borderwidth"] = 5
        self.__text_box.pack()

    def __add_numbers_buttons(self, numbers_buttons_master):
        for n in [7, 8, 9, 4, 5, 6, 1, 2, 3, 0]:  # numbers in order like the numeric keypad
            button = self.__return_default_button(numbers_buttons_master, str(n))
            button["command"] = lambda arg1 = str(n): self.__click_number_button(arg1)

            if n in range(7, 10):  # 7, 8, 9
                row_position = 0
            elif n in range(4, 7):  # 4, 5, 6
                row_position = 1
            elif n in range(1, 4):  # 1, 2, 3
                row_position = 2
            else:
                row_position = 3

            if n in [7, 4, 1]:
                column_position = 0
            elif n in [8, 5, 2, 0]:
                column_position = 1
            else:
                column_position = 2

            button.grid(row=row_position, column=column_position)

    def __add_positive_negative_buttons(self, positive_negative_buttons_master):
        button = self.__return_default_button(positive_negative_buttons_master, "+\n-")
        button["command"] = self.__click_positive_negative_button
        button.grid(row=3, column=0)

    def __add_operation_buttons(self, operation_buttons_master):
        row_position = 0
        for op in self.__OPERATION_SYMBOLS:
            button = self.__return_default_button(operation_buttons_master, op)

            if op == "=":
                button["command"] = self.__click_equal_button
            else:
                button["command"] = lambda arg1=op: self.__set_operation(arg1)

            column_position = 3
            button.grid(row=row_position, column=column_position)

            row_position += 1

    def __add_dot_button(self, dot_button_master):
        button = self.__return_default_button(dot_button_master, ".")
        button["command"] = self.__click_dot_button
        button.grid(row=3, column=2)

    def __add_clear_buttons(self, clear_buttons_master):
        button = self.__return_default_button(clear_buttons_master, "CE")
        button["command"] = self.__clear_display
        button.grid(row=4, column=0)

    def __click_number_button(self, value):
        current_text = self.__entry_text.get()
        self.__entry_text.set(current_text + str(value))

    def __click_positive_negative_button(self):
        number = self.__entry_text.get()
        number = change_signal(number)
        self.__set_display_text(number)

    def __click_equal_button(self):
        self.__NUMBER2 = self.__get_display_text()

        if self.__OPERATION == "+":
            result_from_operation = add(self.__NUMBER1, self.__NUMBER2)
        elif self.__OPERATION == "-":
            result_from_operation = subtract(self.__NUMBER1, self.__NUMBER2)
        elif self.__OPERATION == "*":
            result_from_operation = multiply(self.__NUMBER1, self.__NUMBER2)
        elif self.__OPERATION == "/":
            result_from_operation = divide(self.__NUMBER1, self.__NUMBER2)
        else:
            return

        self.__set_display_text(result_from_operation)
        self.__OPERATION = ""

    def __set_operation(self, value):
        if value in self.__OPERATION_SYMBOLS:
            self.__OPERATION = value
            self.__NUMBER1 = self.__entry_text.get()
            self.__clear_display()
        else:
            self.__OPERATION = ""

    def __click_dot_button(self):
        current_text = self.__entry_text.get()
        if "." not in current_text:
            self.__entry_text.set(current_text + ".")

    def __clear_display(self):
        self.__entry_text.set('')

    def __set_display_text(self, result):
        self.__clear_display()
        self.__entry_text.set(result)

    def __get_display_text(self):
        return self.__entry_text.get()

    def __return_default_button(self, button_master, text_value):
        button = tk.Button(master=button_master, activebackground='gray', bg='white', bd=2)
        button["height"] = self.__BUTTON_HEIGHT
        button["width"] = self.__BUTTON_WIDTH
        button["text"] = text_value
        button["font"] = ("Arial", 10, "bold")
        return button
