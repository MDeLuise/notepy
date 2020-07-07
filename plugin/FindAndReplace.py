import tkinter as tk




class FindReplacePlugin:
    def __init__(self, main):
        self.text = main.text
        self.key_binding_functions()


    def key_binding_functions(self):
        self.text.bind("<Control-f>", self.findall)
        #self.text.bind("<Control-m>", self.findall)
        self.text.bind("<Control-Shift-h>", self.replace_all)
        self.text.bind("<Control-h>", self.replace)
        self.text.bind("<Any-Button>", self.reset_tags)
        return


    def findAsk(self, parent, *args):
        root = tk.Toplevel(parent)
        root.title("Find And Replace")
        root.transient(parent)
        root.focus_force()
        root.resizable(width=0, height=0)
        root['padx']=20
        fields = {}
        field = {}
        
        # create the prompt
        for r, label in enumerate(args):
            store_label = tk.Label(root, text=label)
            store_label.grid(row=r, column=0, ipady=5, ipadx=20)
            store_entry = tk.Entry(root)
            store_entry.grid(row=r, column=1)
            field[label] = store_entry
        fields['submit'] = False

        field[args[0]].focus_set()

        def sub():
            for l,t in field.items():
                fields[l] = t.get()
            fields['submit'] = True
            root.destroy()
            return

        submit=tk.Button(root, text="Ok", command=sub)
        submit.grid(row=r+1, column=2)
        root.wait_window()
        return fields


    def search(self, word):
        if word:
            countvar = tk.StringVar()
            f = self.text.search(word, "1.0", count=countvar)
            starting_index = f
            ending_index = "{}+{}c".format(starting_index, countvar.get())
            self.text.tag_add("search", starting_index, ending_index)
            self.text.tag_configure("search", background="skyblue", foreground="red")
            return True
        else:
            return None


    def reset_tags(self, event=None):
        self.text.tag_delete("search")
        return


    def searchall(self, word):
        index = "1.0"
        if word:
            while True:
                f = self.text.search(word, index, stopindex=tk.END)
                if not f:
                    break
                starting_index =int(f.split(".")[0])
                ending_index  = len(word)+int(f.split(".")[1])
                coordinates = "{}.{}".format(starting_index, ending_index)
                self.text.tag_add("search", f, coordinates)
                self.text.tag_configure("search", background="skyblue", foreground="red")
                index = coordinates
            return True
        else:
            return None


    def replace(self, word):
        if word:
            coordinates=[]
            l=list(self.text.tag_ranges("search"))
            l.reverse()
            while l:
                coordinates.append([l.pop(),l.pop()])
            for start, end in coordinates:
                self.text.delete(start, end)
                self.text.insert(start, word)
        return


    def replace_all(self, word):
        if word:
            coordinates=[]
            l=list(self.text.tag_ranges("search"))
            l.reverse()
            while l:
                coordinates.append([l.pop(),l.pop()])
            for start, end in coordinates:
                self.text.delete(start, end)
                self.text.insert(start, word)
            
        return


    def find(self, event=None):
        t = self.findAsk(self.text.master, "Find")
        if t['submit']:
            self.search(t['Find'])
        return


    def findall(self, event=None):
        t = self.findAsk(self.text.master, "FindAll")
        if t['submit']:
            self.searchall(t['FindAll'])
        return


    def replace(self, event=None):
        t = self.findAsk(self.text.master, "Find", "Replace")
        if t['submit']:
            self.search(t['Find'])
            self.replace_all(t['Replace'])
        return


    def replace_all(self, event=None):
        t = self.findAsk(self.text.master, "FindAll", "ReplaceAll")
        if t['submit']:
            self.searchall(t['FindAll'])
            self.replace_all(t['ReplaceAll'])
        return