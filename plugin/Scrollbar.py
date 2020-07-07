import tkinter as tk



class ScrollbarPlugin():
    def __init__(self, main):
        scrollb = tk.Scrollbar(main.container, command=main.text.yview)
        main.text['yscrollcommand'] = scrollb.set
        scrollb.grid(row=0, column=2, sticky=tk.N+tk.S)
