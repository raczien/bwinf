import tkinter as tk
from contextlib import redirect_stdout
from tkinter.scrolledtext import ScrolledText
import initial_constants as const
import os
import start as s


option_list = os.listdir("gewichte")


class TkConsole(ScrolledText):
    def write(self, text):
        self.insert(tk.END, text)

    def clear_console(self):
        self.delete('1.0', tk.END)


class GUI():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Marktwaage")
        self.rahmen1 = tk.Frame(master=self.root)
        self.rahmen1.pack(side='left', padx='5', pady='5')
        self.label = tk.Label(self.rahmen1, text="Change calculate missing values", font=('Helvetica', 12))
        self.label.pack(side='top', padx='5', pady='5')
        self.find_missing_button = tk.Button(self.rahmen1, text='False', width=15, bg="red", font=('Helvetica', 12), command=lambda: self.changepermute_boolean())
        self.find_missing_button.pack(side='top', padx='5', pady='5')
        self.start_button = tk.Button(self.rahmen1, text='Start', width=15, bg="green", font=('Helvetica', 12), command=lambda: self.start_calculating())
        self.start_button.pack(side='top', padx='5', pady='5')
        self.clear_button = tk.Button(self.rahmen1, text='Clear Console', width=15, font=('Helvetica', 12), command=lambda: self.console.clear_console())
        self.clear_button.pack(side='top', padx='5', pady='5')
        self.console = TkConsole(self.root, width=120, height=40)
        self.console.pack()
        self.variable = tk.StringVar(self.root)
        self.variable.set(option_list[0])
        self.opt = tk.OptionMenu(self.rahmen1, self.variable, *option_list)
        self.opt.config(width=20, font=('Helvetica', 12))
        self.opt.pack()

        with redirect_stdout(self.console):
            print("Bitte links ein Textdokument auswählen.")
            print("True/False Taste ändert den Ausgleich der Waage, inden Gewichte auf die andere Seite gestellt werden.")
            print("Negative Zahlen müssen auf die Linke Seite zu dem zu errechnenden Gewicht gepackt werden, positive auf die andere.")

        self.root.mainloop()

    def start_calculating(self):
        with redirect_stdout(self.console):
            s.start(self.variable.get())

    def changepermute_boolean(self):
        if const.search_for_missing_with_permutation:
            const.search_for_missing_with_permutation = False
            self.find_missing_button.configure(bg="red", text="False")
        elif not const.search_for_missing_with_permutation:
            const.search_for_missing_with_permutation = True
            self.find_missing_button.configure(bg="green", text="True")


app = GUI()
