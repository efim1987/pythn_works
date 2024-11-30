import tkinter as tk
def numbers():
    num1=int(entry1.get())
    num2=int(entry2.get())
    sum_result=num1+num2
    if sum_result%2==0:
        result=(num1**2)-(num2**2)
    else:
        result=(num1-num2)**2
    result_label.config(text=f"Результат: {result}")
root=tk.Tk()
root.title("Вычисление")
entry1_label=tk.Label(root, text="Число 1:")
entry1_label.pack()
entry1=tk.Entry(root)
entry1.pack()
entry2_label=tk.Label(root, text="Число 2:")
entry2_label.pack()
entry2=tk.Entry(root)
entry2.pack()
calculate_button=tk.Button(root, text="Вычислить", command=numbers)
calculate_button.pack(pady=5)
result_label=tk.Label(root, text="", fg="black")
result_label.pack()
root.mainloop()
