#!/user/bin/env python3
"""Will create the buttons and the layout of the buttons for a calculator."""
import customtkinter as ctk


MATH_OPERATORS = {
    "\u00F7": {"col": 1, "row": 0, "operator": "/"},
    "\u00D7": {"col": 2, "row": 0,  "operator": "*"},
    "-": {"col": 3, "row": 1, "operator": "-"},
    "=": {"col": 3, "row": 4, "operator": "="},
    "+": {"col": 3, "row": 2, "operator": "+"},
}


OPERATORS = {
    "AC": {"col": 3, "row": 0, "function": "clear"},
    "\u207A\u2044\u208B": {"col": 3, "row": 3, "function": "pos_neg"},
    "%": {"col": 0, "row": 0, "function": "percent"}
}


class Numbers_Make(ctk.CTkButton):
    col = 0
    row = 3

    def __init__(self, parent, text: int, number: classmethod):
        self.number = number
        super().__init__(parent,
                         font=ctk.CTkFont("Times New Roman", 32),
                         corner_radius=0,
                         text=f"{text}",
                         fg_color="#a958f7",
                         text_color="#ffffff",
                         hover_color="#4161f7",
                         command=lambda: self.number(text))

        if text == 0:
            self.grid(column=0, row=4, columnspan=2, sticky="news", padx=0.5, pady=0.1)
        elif text == ".":
            self.grid(column=2, row=4, sticky="news", padx=0.1, pady=0.1)
        else:
            self.grid(column=Numbers_Make.col, row=Numbers_Make.row, sticky="news", padx=0.1, pady=0.1)
            if Numbers_Make.col < 2:
                Numbers_Make.col += 1
            else:
                Numbers_Make.col = 0
                Numbers_Make.row -= 1


class Math_Make(ctk.CTkButton):
    def __init__(self, parent, key: str, value: dict, method: classmethod):
        super().__init__(parent,
                         text=key,
                         font=("Times New Roman", 32),
                         corner_radius=0,
                         fg_color="#a958f7",
                         text_color="#ffffff",
                         hover_color="#4161f7",
                         command=lambda: method(value["operator"]))
        self.grid(column=value["col"], row=value["row"], sticky="news", padx=0.1, pady=0.1)


class Special_Make(ctk.CTkButton):
    def __init__(self, parent, key: str, value: dict, clear: classmethod, percent: classmethod, change_sign: classmethod):
        this_function = value["function"]
        if this_function == "clear":
            self.method = clear
        elif this_function == "percent":
            self.method = percent
        else:
            self.method = change_sign
        super().__init__(parent,
                         text=key,
                         font=("Times New Roman", 32),
                         corner_radius=0,
                         fg_color="#a958f7",
                         text_color="#ffffff",
                         hover_color="#4161f7",
                         command=lambda: self.method())
        self.grid(column=value["col"], row=value["row"], sticky="news", padx=0.1, pady=0.1)


if __name__ == "__main__":
    print("This is a module.")
    exit()
