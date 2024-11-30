import tkinter as tk
def calculator():
    try:
        num1=float(entry1.get())
        num2=float(entry2.get())
        operation=operation_var.get()
        if operation == "сложение":
            result=num1+num2
        elif operation=="вычитание":
            result=num1-num2
        elif operation=="умножение":
            result=num1*num2
        elif operation=="деление":
            if num2==0:
                result("Делить на 0 нельзя!")
            else:
                 result=num1/num2

        else:
            result="Неверная операция!"
        result_label.config(text=str(result))

    except ValueError:
        result_label.config(text="Ошибка!")

root=tk.Tk()
root.title("Calculator")
entry1=tk.Entry(root, width=10, font=("Segoe UI", 12))
entry1.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
operation_var=tk.StringVar()
operation_var.set("сложение")
operation_menu=tk.OptionMenu(root, operation_var, "сложение", "вычитание", "умножение", "деление")
operation_menu.config(font=("Segoe UI", 12))
operation_menu.grid(row=1, column=0, columnspan=4, padx=5, pady=5, sticky="ew")
entry2=tk.Entry(root, width=10, font=("Segoe UI", 12))
entry2.grid(row=2, column=0, columnspan=4, padx=5, pady=5)
calculate_button=tk.Button(root, text="=", command=calculator, font=("Segoe UI", 12))
calculate_button.grid(row=3, column=0, columnspan=4, padx=5, pady=5, sticky="ew")
result_label=tk.Label(root, text="", font=("Segoe UI", 12), relief="sunken", bd=2, padx=10, pady=5, anchor="e")
result_label.grid(row=4, column=0, columnspan=4, padx=5, pady=5, sticky="ew")
root.mainloop()
