import tkinter as tk
from tkinter import ttk, Tk
import json


class App:
    def __init__(self, master, data):
        self.master = master
        self.master.title("Tree")

        self.tree = ttk.Treeview(self.master)
        self.tree.grid(sticky="nsew")
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)
        first_item = self.tree.insert("", 'end', text="Games")

        self.add_json_data(first_item, data)

    def add_json_data(self, parent, data):
        if isinstance(data, dict):
            for key, value in data.items():
                item = self.tree.insert(parent, 'end', text=str(key))
                self.add_json_data(item, value)
        elif isinstance(data, list):
            for i, item in enumerate(data):
                new_parent = self.tree.insert(parent, 'end', text=str(i))
                self.add_json_data(new_parent, item)
        else:
            self.tree.insert(parent, 'end', text=str(data))


if __name__ == "__main__":
    file_path = "C:\\Users\\41156\Downloads\\video_games.json"

    with open(file_path, "r") as file:
        json_data = json.load(file)

    root = tk.Tk()
    root.geometry("1000x900")
    app = App(root, json_data)
    root.mainloop()
