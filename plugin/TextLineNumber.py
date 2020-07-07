import tkinter as tk



class TextLineNumbers(tk.Canvas):
    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs)
        self.main = None
        self.text = None


    def attach(self, main):
        self.text = main.text
        self.main = main

        self.text.bind("<<Change>>", self._on_change)
        self.text.bind("<Configure>", self._on_change)


    def _on_change(self, event):
        # draw new number
        self._redraw()

        # increase or decrease width of line number section if needed
        total_line_digit = int(self.text.index('end-1c').split('.')[0])
        if self.line_number_digit < len(str(total_line_digit)):
            self.line_number_digit += 1
            self.width += 14
        elif self.line_number_digit > len(str(total_line_digit)):
            self.line_number_digit -= 1
            self.width -= 14

        super().config(width=self.width)


    def _redraw(self, *args):
        '''redraw line numbers'''
        self.delete("all")

        i = self.text.index("@0,0")
        while True:
            dline = self.text.dlineinfo(i)
            if dline is None: break
            y = dline[1]
            linenum = str(i).split(".")[0]
            self.create_text(2, y, anchor="nw", text=linenum, fill="#376875", font=("mono",17))
            i = self.text.index("%s+1line" % i)




class TextLineNumberPlugin():
    def __init__(self, main):
        bg_color = "#073642"
        line_num = 2
        width = 35

        line_numbers = TextLineNumbers(main.container, width=width, bg=bg_color, borderwidth=0)
        
        line_numbers.line_number_digit = line_num
        line_numbers.number_bg_color = bg_color
        line_numbers.attach(main)
        line_numbers.width = width

        main.container.grid_rowconfigure(0, weight=0)
        main.container.grid_columnconfigure(0, weight=0)
        
        main.text.grid_remove()
    
        line_numbers.grid(row=0,column=0,sticky=tk.N+tk.S)
        
        main.text.grid(row=0,column=1,sticky="nsew")

        main.container.grid_rowconfigure(0, weight=1)
        main.container.grid_columnconfigure(1, weight=1)