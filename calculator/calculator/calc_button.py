import tkinter as tk


class CalсButton(tk.Button):
    def __init__(self, *args, **kw):
        kw['bg'] = 'lightblue'
        kw['width'] = 10
        kw['height'] = 2
        super().__init__(*args, **kw)


