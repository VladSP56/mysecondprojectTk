
import tkinter as tk

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.delete(selected_task)


def mark_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.itemconfig(selected_task, bg="DeepSkyBlue")


root = tk.Tk()

root.title("My project")
root.geometry("800x700")

root.configure(background = "chartreuse2")

text1 = tk.Label(root, text = "Enter your task:", bg ="gold")
text1.pack(pady = 5)

task_entry = tk.Entry(root, width = 40,fg = "red", bg = "cornsilk")
task_entry.pack(pady = 10)

add_task_button = tk.Button(root, text = "Add task", command=add_task)
add_task_button.pack(pady = 10)

delete_button = tk.Button(root, text = "Delete", command=delete_task)
delete_button.pack(pady = 10)

mark_button = tk.Button(root, text = "Task completed", command=mark_task)
mark_button.pack(pady =10)

text2 = tk.Label(root, text ="List of tasks:", bg ="gold")
text2.pack(pady = 5)

task_listbox = tk.Listbox(root, height = 100, width = 500, bg ="grey")
task_listbox.pack(pady =10)



root.mainloop()




