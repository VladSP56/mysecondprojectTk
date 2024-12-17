from tkinter import Tk, Button

root = Tk()
button1 = Button(root, text = "button 1")
button2 = Button(root, text = "button 2")
button1.grid(row = 0, column = 2)
button2.grid(row = 1, column = 0)
root.mainloop()
