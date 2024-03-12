import tkinter as tk
from tkinter import messagebox
from calc_button import CalсButton
from calc_entry import CalcEntry
import math


def main():
    def calculate():
        result = get_calculated()
        insert_result(result)

    def get_calculated():
        try:
            result = eval(entry.get())
            return result
        except Exception as e:
            messagebox.showerror("Ошибка", "Неверное выражение")
            result_entry.insert(0, "")

    def insert_result(result):
        result_entry.delete(0, tk.END)
        result_entry.insert(tk.END, "" + str(result))

    def calc_sec():
        result = get_calculated()
        insert_result(1 / math.cos(result))

    def calc_divide():
        last = entry.get()[-1]
        if last in "0123456789":
            entry.insert(tk.END, "/")

    def clear():
        entry.delete(0, tk.END)
        result_entry.delete(0, tk.END)

    def on_closing():
        if messagebox.askokcancel("Выход", "Вы уверены, что хотите выйти?"):
            root.destroy()

    root = tk.Tk()
    root.title("калькулятор")

    entry = CalcEntry(root)
    entry.grid(row=0, column=0, columnspan=3)

    result_entry = tk.Entry(root)
    result_entry.grid(row=1, column=0, columnspan=3)

    sec_button = CalсButton(root, text="sec", command=calc_sec)
    sec_button.grid(row=3, column=0)

    divide_button = CalсButton(root, text="/", command=calc_divide)
    divide_button.grid(row=3, column=1)

    calculate_button = CalсButton(root, text="Вычислить", command=calculate)
    calculate_button.grid(row=3, column=2)

    clear_button = CalсButton(root, text="Стереть", command=clear)
    clear_button.grid(row=3, column=3)

    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()


if __name__ == '__main__':
    main()
