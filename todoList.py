import tkinter as todoList 


class ToDoList(todoList.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.tasks = []

        self.label = todoList.Label(self, text="ToDo List")
        self.label.pack()

        self.entry = todoList.Entry(self)
        self.entry.pack()

        self.button = todoList.Button(
            self, text="Add Task", command=self.add_task)
        self.button.pack()

        self.listbox = todoList.Listbox(self)
        self.listbox.pack()
        
        self.delete_button = todoList.Button(
            self, text="Delete", command=self.delete_task)
        self.delete_button.pack()


    def add_task(self):
        task = self.entry.get()
        self.tasks.append(task)
        self.listbox.insert(todoList.END, task)

        self.entry.delete(0, todoList.END)
        
    def delete_task(self):
        selected_task = self.listbox.get(todoList.ACTIVE)
        self.listbox.delete(todoList.ACTIVE)
        self.tasks.remove(selected_task)


root = todoList.Tk()
todo_list = ToDoList(root)
todo_list.pack()
root.mainloop()