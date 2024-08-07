#to_do_list
#importing 
#importing tkinter for GUI
#importing messagebox for popup messages 
#importing datetime for date and time
import tkinter as tk
from tkinter import messagebox
import datetime

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = []

        self.frame = tk.Frame(root)
        self.frame.pack()

        self.title_label = tk.Label(self.frame, text="To-Do List", font=("verdana", 18))
        self.title_label.pack(pady=10)

        self.task_entry = tk.Entry(self.frame, width=50)
        self.task_entry.pack(pady=10)
#button to add a task
        self.add_task_button = tk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=5)
#button to update a task
        self.update_task_button = tk.Button(self.frame, text="Update Task", command=self.update_task)
        self.update_task_button.pack(pady=5)
#button to delete a task
        self.delete_task_button = tk.Button(self.frame, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack(pady=5)

        self.tasks_listbox = tk.Listbox(self.frame, width=50, height=15)
        self.tasks_listbox.pack(pady=10)

        self.date_label = tk.Label(self.frame, text="", font=("verdana", 12))
        self.date_label.pack(pady=10)

        self.update_date_time()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")
#updation
    def update_task(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            new_task = self.task_entry.get()
            if new_task:
                self.tasks[selected_task_index[0]] = new_task
                self.update_task_listbox()
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "You must enter a task.")
        else:
            messagebox.showwarning("Warning", "You must select a task to update.")
#deletion
    def delete_task(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            del self.tasks[selected_task_index[0]]
            self.update_task_listbox()
            #warning messagebox
        else:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def update_task_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.tasks_listbox.insert(tk.END, task)

    def update_date_time(self):
        now = datetime.datetime.now()
        self.date_label.config(text=f"{now.strftime('%Y-%m-%d %H:%M:%S')}")
        self.root.after(1000, self.update_date_time)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
