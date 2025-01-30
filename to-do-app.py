import tkinter as tk
from tkinter import messagebox

# Main window
root = tk.Tk()
root.title("To-Do App")
root.geometry("400x300")

# Tasks list
tasks = []

# Functions
def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        update_task_list()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        selected_task = listbox.curselection()[0]
        tasks.pop(selected_task)
        update_task_list()
    except:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def update_task_list():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

# UI Elements
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

listbox = tk.Listbox(root, width=40)
listbox.pack(pady=10)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

# Run the app
root.mainloop()