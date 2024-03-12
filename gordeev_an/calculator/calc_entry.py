import tkinter as tk


class CalcEntry(tk.Entry):
    def __init__(self, master=None, allowed_chars='+-*/()0123456789', **kwargs):
        self.allowed_chars = set(allowed_chars)
        super().__init__(master, **kwargs)

        inp = (self.register(self.validate_input), '%P')
        self.config(validate='key', validatecommand=inp)

    def validate_input(self, new_text):
        if all(char in self.allowed_chars for char in new_text):
            return True
        self.bell()
        return False