from tkinter import *

class SimpleCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("400x600")

        # Entry widget for displaying the expression
        self.expression = ""
        self.result_var = StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Entry widget to show the result
        self.result_entry = Entry(self.root, textvariable=self.result_var, font=('arial', 20, 'bold'), bd=20, insertwidth=4, width=14, justify='right')
        self.result_entry.grid(row=0, column=0, columnspan=4)

        # Button layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0, 4)  # Clear button spanning all columns
        ]

        for (text, row, col, *colspan) in buttons:
            colspan = colspan[0] if colspan else 1
            button = Button(self.root, text=text, padx=20, pady=20, font=('arial', 18, 'bold'), bd=8, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, columnspan=colspan)

    def on_button_click(self, button_text):
        if button_text == 'C':
            self.expression = ""
            self.result_var.set("")
        elif button_text == '=':
            try:
                # Evaluate the expression
                result = str(eval(self.expression))
                self.result_var.set(result)
                self.expression = result
            except Exception:
                self.result_var.set("Error")
                self.expression = ""
        else:
            self.expression += button_text
            self.result_var.set(self.expression)

def main():
    root = Tk()
    app = SimpleCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
