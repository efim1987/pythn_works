import tkinter as tk
def register():
    last_name=last_name_entry.get()
    first_name=first_name_entry.get()
    password=password_entry.get()

    if last_name and first_name and password:
        result_lable.config(text="Пользователь успешно зарегистрирован.", fg="green")
    else:
        missing_field=[]
        if not last_name:
            missing_field.append("Фамилия")
        if not first_name:
            missing_field.append("Имя")
        if not password:
            missing_field.append("Пароль")
        result_lable.config(text=f"Пропущены поля: {','.join(missing_field)}", fg="red")
root=tk.Tk()
root=title("Форма регистрации")
last_name_label=tk.Label(root, text="Фамилия")
last_name_label.grid(row=0, calumn=0, sticky="e", padx=5, pady=5)
last_name_entry=tk.Entry(root)
