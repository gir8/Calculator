#!/user/bin/env python3
"""This should be the main file and not a module.  This program creates a fully functioning calculator."""
from calc_log_sh import *
import customtkinter as ctk
import tkinter as tk


class Calc_Body(ctk.CTk):
    def __init__(self):
        # window setup
        super().__init__(fg_color="#FF0095")
        self.geometry("300x500")
        self.resizable(False, False)
        try:
            self.title("Calculator")
            self.icon = tk.PhotoImage(file="muffin.png")
            self.wm_iconbitmap()
            self.iconphoto(True, self.icon)
        except Exception:
            pass

        # grid
        self.columnconfigure(0, weight="1", uniform="a")
        self.rowconfigure(0, weight="1")
        self.rowconfigure(1, weight="2")

        # data var
        self.answer_var = ctk.StringVar(value="")
        self.input_var = ctk.StringVar(value="0")
        self.display_numbers = []
        self.full_operation = []

        # create interface
        self.create_frames()
        self.create_screen(self.answer_var, self.input_var)
        self.create_buttons()

    def clear(self):
        if self.input_var.get() != "0":
            self.input_var.set("0")
            self.display_numbers.clear()
        else:
            self.answer_var.set("")
            self.display_numbers.clear()
            self.full_operation.clear()

    def round_zero(self, value: str):
        if value[-2:] == ".0":
            return str(int(float(value)))
        elif value[-1] == ".":
            return str(int(float(value[:-1])))
        else:
            return value

    def percent(self):
        current_number = "".join(self.display_numbers)
        try:
            current_number = float(current_number)
        except ValueError:
            pass
        if current_number and (0 < current_number or 0 > current_number):
            try:
                self.display_numbers = [self.round_zero(str(eval(str(current_number) + "/100")))]
                self.input_var.set(str("".join(self.display_numbers))[:10])
            except Exception:
                pass

    def change_sign(self):
        current_number = "".join(self.display_numbers)
        try:
            current_number = float(current_number)
        except ValueError:
            pass
        if current_number and (0 > current_number or 0 < current_number):
            self.display_numbers = [self.round_zero(str(eval("-1 *" + str(current_number))))]
            self.input_var.set(self.display_numbers)

    def number(self, value: int):
        # prevent more than one .
        if value == "." and value in self.display_numbers:
            pass
        # change . to 0.
        elif value == "." and self.display_numbers == []:
            self.display_numbers.append("0")
            self.display_numbers.append(str(value))
            full_number = "".join(self.display_numbers)
            self.input_var.set(full_number)
        else:
            if len(self.display_numbers) == 1 and value != "." and self.display_numbers[0] == "0":
                self.display_numbers.pop(0)
            self.display_numbers.append(str(value))
            full_number = "".join(self.display_numbers)
            self.input_var.set(full_number)

    def math_symbols(self, symbol: str):
        current_number = "".join(self.display_numbers)

        # swapping math symbols
        if self.answer_var and symbol != "=" and not current_number:
            equation = self.answer_var.get()
            try:
                if equation[-1] in ["+", "/", "*", "-"]:
                    self.answer_var.set(equation[:-1] + symbol)
                    self.full_operation.pop()
                    self.full_operation.append(symbol)
            except:
                pass

        if current_number:
            self.full_operation.append(self.round_zero(current_number))
            if symbol != "=":
                # update data
                self.full_operation.append(self.round_zero(symbol))
                self.display_numbers.clear()

                # update output
                self.input_var.set("")
                self.answer_var.set(" ".join(self.full_operation))

            else:
                try:
                    answer = self.round_zero(str(eval("".join(self.full_operation))))
                    # update output
                    self.input_var.set(str(answer)[:7])
                    self.answer_var.set(" ".join(self.full_operation))

                    self.display_numbers = [str(answer)]
                    self.full_operation.clear()
                except ZeroDivisionError:
                    self.full_operation.pop()
                    pass

    def create_frames(self):
        # create screen
        self.screen = ctk.CTkFrame(master=self, fg_color="#000000", corner_radius=0)
        self.screen.columnconfigure(0, weight="1")
        self.screen.rowconfigure(list(range(2)), weight="1")
        self.screen.grid(column=0, row=0, sticky="news")

        # create buttons frame
        self.button_frame = ctk.CTkFrame(master=self, fg_color="transparent")
        self.button_frame.columnconfigure(list(range(4)), weight="1", uniform="a")
        self.button_frame.rowconfigure(list(range(5)), weight="1", uniform="a", pad=10)
        self.button_frame.grid(column=0, row=1, sticky="news", pady=1)

    def create_screen(self, var_a: ctk.StringVar, var_b: ctk.StringVar):
        answer_label = ctk.CTkLabel(master=self.screen,
                                    font=("Times New Roman", 32),
                                    text=None, text_color="#00ff00",
                                    bg_color="#000000",
                                    textvariable=var_a)
        answer_label.grid(column=0, row=0, sticky="nes", padx=10)

        input_label = ctk.CTkLabel(master=self.screen,
                                   font=("Times New Roman", 70),
                                   text=None, text_color="#00ff00",
                                   bg_color="#000000",
                                   textvariable=var_b)
        input_label.grid(column=0, row=1, sticky="se", padx=10, pady=5)

    def create_buttons(self):
        # create numbers
        for i in range(10):
            Numbers_Make(self.button_frame, i, self.number)
        # create .
        Numbers_Make(self.button_frame, ".", self.number)

        # create special buttons
        for key, value in OPERATORS.items():
            Special_Make(self.button_frame, key, value, self.clear, self.percent, self.change_sign)

        # create operator symbols
        for key, value in MATH_OPERATORS.items():
            Math_Make(self.button_frame, key, value, self.math_symbols)

    def run(self):
        self.mainloop()


if __name__ == "__main__":
    calculator = Calc_Body()
    calculator.run()

if __name__ == "__module__":
    print("This file should be the main.")
    exit()
