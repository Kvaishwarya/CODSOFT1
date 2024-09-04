from tkinter import *
from tkinter import ttk

class Todo:
    def __init__(self, root):
        self.root = root
        self.root.title('TO-DO LIST')
        self.root.geometry('650x410+300+150')

        # Title and Labels
        self.label = Label(self.root, text='To-DO-List-app', font='ariel', width=10, bd=5, bg='orange', fg='black')
        self.label.pack(side='top', fill=BOTH)

        self.label2 = Label(self.root, text='Add task', font='ariel', width=10, bd=5, bg='orange', fg='black')
        self.label2.pack(side='top', fill=BOTH)
        self.label2.place(x=40, y=54)

        self.label3 = Label(self.root, text='Task', font='ariel', width=10, bd=5, bg='orange', fg='black')
        self.label3.pack(side='top', fill=BOTH)
        self.label3.place(x=320, y=54)

        # Listbox and Text widgets
        self.main_text = Listbox(self.root, height=9, width=50, bd=5, font='ariel', fg='black')  # Set text color to black
        self.main_text.place(x=280, y=100)

        self.text = Text(self.root, bd=5, height=2, width=30, font='ariel, 10 bold')
        self.text.place(x=20, y=120)

        # Buttons
        self.button_add = Button(self.root, text="ADD", font='sarif', width=10, bd=5, bg='orange', fg='black', command=self.add_task)
        self.button_add.place(x=30, y=180)

        self.button_delete = Button(self.root, text="DELETE", font='sarif', width=10, bd=5, bg='orange', fg='black', command=self.delete_task)
        self.button_delete.place(x=30, y=280)

        self.button_update = Button(self.root, text="UPDATE", font='sarif', width=10, bd=5, bg='orange', fg='black', command=self.update_task)
        self.button_update.place(x=150, y=180)

        # Load existing tasks from file
        self.load_tasks()

    def add_task(self):
        content = self.text.get(1.0, END).strip()
        if content:
            self.main_text.insert(END, content)
            with open('data.txt', 'a') as file:
                file.write(content + '\n')
            self.text.delete(1.0, END)

    def delete_task(self):
        try:
            selected_index = self.main_text.curselection()[0]
            selected_task = self.main_text.get(selected_index)
            self.main_text.delete(selected_index)
            self.update_file()
        except IndexError:
            pass  # No task selected

    def update_task(self):
        try:
            selected_index = self.main_text.curselection()[0]
            updated_task = self.text.get(1.0, END).strip()
            if updated_task:
                self.main_text.delete(selected_index)
                self.main_text.insert(selected_index, updated_task)
                self.update_file()
                self.text.delete(1.0, END)
        except IndexError:
            pass  # No task selected

    def load_tasks(self):
        try:
            with open('data.txt', 'r') as file:
                tasks = file.readlines()
                for task in tasks:
                    self.main_text.insert(END, task.strip())
        except FileNotFoundError:
            pass

    def update_file(self):
        tasks = self.main_text.get(0, END)
        with open('data.txt', 'w') as file:
            for task in tasks:
                file.write(task + '\n')

def main():
    root = Tk()
    app = Todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()
