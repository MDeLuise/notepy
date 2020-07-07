import tkinter as tk




class RightClickPlugin:
    def __init__(self, main):
        self.text = main.text
        self.functions_binding_key()
        self.functions_configurations()

    def functions_configurations(self):
        self.menu = tk.Menu(self.text, tearoff=False)
        self.menu.add_command(label="Copy", command=lambda: self.text.event_generate("<<Copy>>"))
        self.menu.add_command(label="Cut", command=lambda: self.text.event_generate("<<Cut>>"))
        self.menu.add_command(label="Paste", command=lambda: self.text.event_generate("<<Paste>>"))
        self.menu.add_separator()
        self.menu.add_command(label="Select All", command=lambda: self.text.tag_add("sel",'1.0','end'))
        self.menu.add_separator()
        return

    def functions_binding_key(self):
        self.text.bind("<Button-3>",self.show_menu)
        return

    def show_menu(self, event):
        self.menu.tk_popup(event.x_root, event.y_root)
        return