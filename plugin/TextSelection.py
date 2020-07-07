import tkinter as tk




class TextSelectionPlugin:
    
    def __init__(self, main):

        self.text = main.text

        self.text.tag_configure("sel", background="skyblue")
        
        editMenu = tk.Menu(main["menubar"], tearoff=False)
        main["menubar"].add_cascade(label="Edit", menu=editMenu)
        editMenu.add_command(label="Redo", command=self.redo, accelerator="Ctrl+Shift+Z")
        editMenu.add_command(label="Undo", command=self.undo, accelerator="Ctrl+Z")
        editMenu.add_separator()
        editMenu.add_command(label="Copy", command=self.copy, accelerator="Ctrl+C")
        editMenu.add_command(label="Cut", command=self.cut, accelerator="Ctrl+X")
        editMenu.add_command(label="Paste", command=self.paste, accelerator="Ctrl+V")
        editMenu.add_separator()
        editMenu.add_command(label="Select All", command=self.select_all, accelerator="Ctrl+A")
        editMenu.add_command(label="Deselect All", command=self.deselect_all)

        main.text.bind("<Control-z>", lambda _: self.undo())
        main.text.bind("<Control-Shift-z>", lambda _: self.redo())
        main.text.bind("<Control-a>", lambda _: self.select_all())

        # below already defined in tkinter
        #main.text.bind("<Control-c>", lambda _: self.copy())
        #main.text.bind("<Control-x>", lambda _: self.cut())
        #main.text.bind("<Control-v>", lambda _: self.paste())


    def copy(self, event=None):
        self.text.event_generate("<<Copy>>")
        return


    def paste(self, event=None):
        self.text.event_generate("<<Paste>>")
        return


    def cut(self, event=None):
        self.text.event_generate("<<Cut>>")
        return


    def undo(self, event=None):
        self.text.event_generate("<<Undo>>")
        return


    def redo(self, event=None):
        self.text.event_generate("<<Redo>>")
        return


    def select_all(self, event=None):
        self.text.tag_add("sel",'1.0','end')
        return "break" # apparently because Control-a is bind to "return at starting line"


    def deselect_all(self, event=None):
        self.text.tag_remove("sel",'1.0','end')
        return