import tkinter as tk

root = tk.Tk()
root.title("Summ of numbers")

label = tk.Label(root, text = "Put numbers separated with space")
label.pack(pady = 10)

entry = tk.Entry(root)
entry.pack(pady = 10)

root.mainloop()