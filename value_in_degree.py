import tkinter as tk
def value():
    a=int(entry.get())
    power=scale.get()
    result=a**power
    result_label.config(text=f"Результат: {result}")
root=tk.Tk()
root.title("Число в степени...")
entry=tk.Entry(root)
entry.pack(pady=5)
scale=tk.Scale(root, from_=0, to=5, orient=tk.HORIZONTAL, label="степень:")
scale.pack(pady=5)
calculate_button=tk.Button(root, text="Вычислить", command=value)
calculate_button.pack(pady=5)
result_label=tk.Label(root, text="", fg="black")
result_label.pack()
root.mainloop()
