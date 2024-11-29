import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")

        # Create a frame for the form
        self.form_frame = tk.Frame(root)
        self.form_frame.pack(pady=10)

        # Create a title label and entry
        self.title_label = tk.Label(self.form_frame, text="Title:")
        self.title_label.grid(row=0, column=0, padx=5, pady=5)
        self.title_entry = tk.Entry(self.form_frame)
        self.title_entry.grid(row=0, column=1, padx=5, pady=5)

        # Create a description label and entry
        self.desc_label = tk.Label(self.form_frame, text="Description:")
        self.desc_label.grid(row=1, column=0, padx=5, pady=5)
        self.desc_entry = tk.Entry(self.form_frame)
        self.desc_entry.grid(row=1, column=1, padx=5, pady=5)

        # Create Add Task button
        self.add_button = tk.Button(self.form_frame, text="Add Task", command=self.add_task)
        self.add_button.grid(row=2, columnspan=2, pady=10)

        # Create a listbox to show tasks
        self.task_listbox = tk.Listbox(root, width=50)
        self.task_listbox.pack(pady=10)

        # Bind double-click event to edit task
        self.task_listbox.bind("<Double-1>", self.edit_task)

        # Create a delete button
        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        # Create a complete button
        self.complete_button = tk.Button(root, text="Mark as Complete", command=self.mark_complete)
        self.complete_button.pack(pady=5)

        # Load tasks from file
        self.tasks = []
        self.load_tasks()

    def add_task(self):
        title = self.title_entry.get()
        description = self.desc_entry.get()

        if title and description:
            self.tasks.append({"title": title, "description": description, "completed": False})
            self.update_task_list()
            self.title_entry.delete(0, tk.END)
            self.desc_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Both fields must be filled.")

    def edit_task(self, event):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task = self.tasks[selected_index[0]]
            new_title = simpledialog.askstring("Edit Task", "New Title:", initialvalue=task["title"])
            new_description = simpledialog.askstring("Edit Task", "New Description:", initialvalue=task["description"])

            if new_title and new_description:
                self.tasks[selected_index[0]] = {"title": new_title, "description": new_description, "completed": task["completed"]}
                self.update_task_list()

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            del self.tasks[selected_index[0]]
            self.update_task_list()

    def mark_complete(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task = self.tasks[selected_index[0]]
            task["completed"] = not task["completed"]
            self.update_task_list()

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "[Completed]" if task["completed"] else "[Pending]"
            self.task_listbox.insert(tk.END, f"{task['title']} - {task['description']} {status}")

    def load_tasks(self):
        # Load tasks from a file or any other storage (implement file handling if needed)
        pass

    def save_tasks(self):
        # Save tasks to a file (implement file handling if needed)
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
