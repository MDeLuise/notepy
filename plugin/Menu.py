import tkinter as tk




class MenuPlugin():
    def __init__(self, main):
        menubar = tk.Menu(main.root)
        main.root.config(menu=menubar)

        main["menubar"] = menubar