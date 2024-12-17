
import tkinter as tk
from tkinter import messagebox

def greet():
    name = entry.get()  # Получаем имя из поля ввода
    if name:  # Проверяем, что имя не пустое
        messagebox.showinfo("Приветствие", f"Привет, {name}!")
    else:
        messagebox.showwarning("Предупреждение", "Пожалуйста, введите свое имя.")

# Создаем главное окно
root = tk.Tk()
root.title("Приветствие")

# Создаем метку
label = tk.Label(root, text="Введите ваше имя:")
label.pack(pady=10)

# Создаем поле ввода
entry = tk.Entry(root)
entry.pack(pady=10)

# Создаем кнопку для приветствия
greet_button = tk.Button(root, text="Поздороваться", command=greet)
greet_button.pack(pady=10)

# Запускаем главный цикл приложения
root.mainloop()