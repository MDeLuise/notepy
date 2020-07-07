import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox




class FileHandlerPlugin():
    def __init__(self, main):
        self.main = main
        self.text = main.text

        self.main["file_saved"] = ""
        self.main.root.title("Untitled - Notepy")

        menubar = main["menubar"]

        self.main.exit_app = self.new_exit(self.main.exit_app)

        fileMenu = tk.Menu(menubar, tearoff=False)
        menubar.add_cascade(label="File", menu=fileMenu)
        fileMenu.add_command(label="New", command=self.open_file, accelerator="Ctrl+N")
        fileMenu.add_command(label="Open", command=self.open_file, accelerator="Ctrl+O")
        fileMenu.add_separator()
        fileMenu.add_command(label="Save", command=self.save_file, accelerator="Ctrl+S")
        fileMenu.add_command(label="Save as", command=self.save_as, accelerator="Ctrl+Shift+S")
        fileMenu.add_separator()
        fileMenu.add_command(label="Quit", command=self.main.exit_app, accelerator="Ctrl+Q")

        main.root.bind("<Control-o>", lambda _: self.open_file())
        main.root.bind("<Control-s>", lambda _: self.save_file())
        main.text.bind("<Control-Shift-S>", lambda _: self.save_as())
        self.text.bind("<KeyRelease>", lambda a: self.key_release(self, a))


    def open_file(self, file=None):
        old_filename = self.main["filename"] if "filename" in self.main else "Untitled"
        self.main["filename"] = file
        
        if not file:
            self.main["filename"] = askopenfilename()

        # needed if file is loaded and new open is clicked (but cancelled)
        if not self.main["filename"]: 
            self.main["filename"] = old_filename
            return

        self.main.clean()
        with open(self.main["filename"],'r') as file_obj:
            self.text.insert(1.0, file_obj.read())
            self.main["file_saved"] = self.text.get(1.0, 'end-1c')

        self.main.root.title(f"{self.main['filename']} - Notepy")
        self.text.edit_reset() # so cannot undo a open file


    def save_file(self):
        text = self.text.get(1.0, 'end-1c')
        if not "filename" in self.main or not self.main["filename"]:
            self.main["filename"] = asksaveasfilename(defaultextension=".txt")

        if not self.main["filename"]: return False

        with open(self.main["filename"],'w') as file_obj:
            file_obj.write(text)
            self.main["file_saved"] = text

        self.main.root.title(f"{self.main['filename']} - Notepy")
        self.text.edit_reset() # so cannot undo after saving the file
        return True


    def save_as(self):
        filename = self.main["filename"] if "filename" in self.main else None
        self.main["filename"] = None
        self.save_file()
        self.main["filename"] = filename


    def key_release(self, event, char):
        saved = "*" if self.is_file_changed() else ""
        
        self.main.root.title(
            f"{saved}{self.main['filename'] if 'filename' in self.main else 'Untitled'}" +
            " - Notepy")


    def is_file_changed(self):
        return self.main["file_saved"] != self.text.get(1.0, 'end-1c')


    def new_exit(self, fun):
        def decorator():
            if not self.is_file_changed():
                fun()
            else:
                ask = messagebox.askyesnocancel(title="Save Changes",
                    message="Do you want to save the changes before closing?")
                if ask == True:
                    saved = self.save_file()
                    if saved: fun()
                elif ask == False:
                    fun()
        return decorator