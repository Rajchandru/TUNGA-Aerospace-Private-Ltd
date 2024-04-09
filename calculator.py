import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        
        self.root.configure(bg='#333')
        
        self.result_entry = tk.Entry(root, font=('Arial', 24), justify='right')
        self.result_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=20, sticky='ew')
        
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]
        
        for (text, row, col) in buttons:
            btn = tk.Button(root, text=text, width=5, height=2, font=('Arial', 14), bg='#666', fg='white', bd=0, command=lambda t=text: self.on_button_click(t))
            btn.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')
        
        for i in range(5):
            root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)
    
    def on_button_click(self, text):
        if text == 'C':
            self.result_entry.delete(0, tk.END)
        elif text == '=':
            try:
                result = eval(self.result_entry.get())
                self.result_entry.delete(0, tk.END)
                self.result_entry.insert(tk.END, str(result))
            except:
                self.result_entry.delete(0, tk.END)
                self.result_entry.insert(tk.END, "Error")
        else:
            self.result_entry.insert(tk.END, text)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
