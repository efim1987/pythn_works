import tkinter as tk
from tkinter import messagebox
def calculator():
    try:
        num1=float(entry1.get())
        num2=float(entry2.get())
        operation=operator.get()
        if operation=="+":
            result=num1+num2
        elif operation=="-":
            result=num1-num2
        elif operation=="*":
            result=num1*num2
        elif operation=="/":
            if num2==0:
                messagebox.showerror("Ошибка", "Делить на 0 нельзя")
                return 
            result=num1/num2
        else:
            messagebox.showerror("Ошибка", "Неверная операция")
            return 
        result_label.config(text="Результат:"+str(result))
    except ValueError:
        messagebox.showerror("Ошибка", "Введите числа")
root=tk.Tk()
root.title("Калькулятор")
entry1_label=tk.Label(root, text="Число1:")
entry1_label.grid(row=0, column=0)
entry1=tk.Entry(root)
entry1.grid(row=0, column=1)
entry2_label=tk.Label(root, text="Число2:")
entry2_label.grid(row=1, column=0)
entry2=tk.Entry(root)
entry2.grid(row=1, column=1)
operator_label=tk.Label(root, text="+, -, *, /")
operator_label.grid(row=2, column=1)
operator=tk.Entry(root)
operator.grid(row=2, column=1)
calculate_button=tk.Button(root, text="Вычислить", command=calculator)
calculate_button.grid(row=4, column=0, columnspan=2)
result_label=tk.Label(root, text="", fg="black")
result_label.grid(row=4, column=0, columnspan=2)
root.mainloop()
