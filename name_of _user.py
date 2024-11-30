import tkinter as tk
from tkinter import messagebox
def user_name():
    name=entry.get()
    if name:
        messagebox.showinfo("Приветствие", f"Привет, {name}")
    else:
        messagebox.showwarning("Предупреждение", "Пожалуйста, введите своё имя")
root=tk.Tk()
root.title("Подтверждение имени пользователя")
label=tk.Label(root, text="Введите ваше имя")
label.pack()
entry=tk.Entry(root)
entry.pack(pady=5)
button=tk.Button(root, text="Приветствовать", command=user_name)
button.pack(pady=5)
root.mainloop()
