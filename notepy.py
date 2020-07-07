import sys

from CustomText import CustomText

import tkinter as tk
from tkinter import Text, BOTH, Label, YES, Menu, END
from tkinter.font import Font



class Notepy():

    def __init__(self, plugins=[], pos=None):
        self._plugin_vars = {}
        self._start_GUI(pos)
        
        # adding plugins
        for pl in plugins:
            pl(self)
        
        self.text.focus_set()
        self.root.mainloop()


    def __setitem__(self, key, item):
        self._plugin_vars[key] = item

    def __getitem__(self, key):
        return self._plugin_vars[key]

    def __contains__(self, key):
        return key in self._plugin_vars


    def _start_GUI(self, pos):
        self.root = tk.Tk()
        self.root.resizable(True, True)
        self.root.title("Notepy")
        self.root.protocol('WM_DELETE_WINDOW', lambda: self.exit_app())

        size_x, size_y = (1000, 800)
        
        if pos:
            self.root.geometry(f'{size_x}x{size_y}+{pos[0]}+{pos[1]}')

        # container needed for increade/decrease font without modify even the window
        self.container = tk.Frame(self.root, borderwidth=0, width=1000, height=800)
        self.container.grid_propagate(False)
        self.container.pack(side="bottom", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        
        self.font = Font(family="mono", size=15)
        self.text_color = "#91a1a1"
        self.bg_color = "#002b36"


        self.text = CustomText(self.container, bg=self.bg_color, fg=self.text_color, undo=True,
            font=self.font, blockcursor=True, insertbackground=self.text_color)
        
        self.text.grid(row=0, column=0, sticky="nsew")

        self._create_shortcuts()



    def _changefont_size(self, increase=True):
        if increase:
            self.font["size"] += 2
        elif self.font["size"] > 5:
            self.font["size"] -= 2


    def _create_shortcuts(self):
        self.root.bind("<Control-q>", lambda _: self.exit_app())
        self.root.bind("<Control-plus>", lambda _: self._changefont_size())
        self.root.bind("<Control-minus>", lambda _: self._changefont_size(increase=False))


    def clean(self):
        self.text.delete('1.0', END)


    def exit_app(self):
        self.root.destroy()