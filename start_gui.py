import tkinter as tk
from contextlib import redirect_stdout
from tkinter.scrolledtext import ScrolledText
import initial_constants as const
import os
import start_marktwaage as s


option_list = os.listdir("gewichte")


class TkConsole(ScrolledText):
    def write(self, text):
        self.insert(tk.END, text)

    def clear_console(self):
        self.delete('1.0', tk.END)


# gui class for easy usage
class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Marktwaage")
        self.rahmen1 = tk.Frame(master=self.root)
        self.rahmen1.pack(side='left', padx='5', pady='5')
        self.clear_button = tk.Button(self.rahmen1, text='Clear Console', width=15, font=('Helvetica', 12), command=lambda: self.console.clear_console())
        self.clear_button.pack(side='top', padx='5', pady='5')
        self.console = TkConsole(self.root, width=120, height=40)
        self.console.pack()
        self.variable = tk.StringVar(self.root)
        self.variable.set(option_list[0])
        self.opt = tk.OptionMenu(self.rahmen1, self.variable, *option_list)
        self.opt.config(width=20, font=('Helvetica', 12))
        self.opt.pack()
        self.start_button = tk.Button(self.rahmen1, text='Start', width=15, bg="green", font=('Helvetica', 12), command=lambda: self.start_calculating())
        self.start_button.pack(side='top', padx='5', pady='5')

        with redirect_stdout(self.console):
            print("Bitte links ein Textdokument auswählen.")
            print("Negative Zahlen müssen auf die Linke Seite zu dem zu errechnenden Gewicht gepackt werden, positive auf die andere.")
            print("Berechnungszeit:\nDokument 0: ~6 Sek\nDokument 1: ~0.03 Sek\nDokument 2: ~0.03 Sek"
                  "\nDokument 3: ~7 Sek\nDokument 4: ~1 Sek\nDokument 5: ~300 Sekunden")

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
