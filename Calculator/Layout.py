import tkinter as tk


class Calculator:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title = "Calculator"
        self.main_window.positionfrom()

        background = tk.Frame(master=self.main_window, width=300, height=500, bg='white')

        self.__add_text_box(self.main_window)
        self.__add_numbers_buttons(background)

        background.pack()

    def __add_text_box(self, text_box_master):
        self.entry_text = tk.StringVar()
        self.text_box = tk.Entry(master=text_box_master, bg='white', width=50, justify='right', textvariable=self.entry_text)
        self.text_box.pack()

    def __click_number_button(self, value):
        current_text = self.entry_text.get()
        self.entry_text.set(current_text + str(value))

    def __add_numbers_buttons(self, numbers_buttons_master):
        for n in [7, 8, 9, 4, 5, 6, 1, 2, 3, 0]:  # numbers in order like the numeric keypad
            button = tk.Button(master=numbers_buttons_master, activebackground='gray', bg='white')
            button["height"] = 3
            button["width"] = 5
            button["text"] = str(n)
            button["command"] = lambda arg1 = str(n): self.__click_number_button(arg1)

            if n in range(7, 10):  # 7, 8, 9
                row_position = 0
            elif n in range(4, 7):  # 4, 5, 6
                row_position = 1
            elif n in range(1, 4):  # 1, 2, 3
                row_position = 2
            else:
                row_position = 3

            if n in [7, 4, 1, 0]:
                column_position = 0
            elif n in [8, 5, 2]:
                column_position = 1
            else:
                column_position = 2

            button.grid(row=row_position, column=column_position)
