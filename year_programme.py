import tkinter as tk
def month_name():
    month_number=int(entry.get())
    if month_number==1:
        result_label.config(text="Январь")
    elif month_number==2:
        result_label.config(text="Февраль")
    elif month_number==3:
        result_label.config(text="Март")
    elif month_number==4:
        result_label.config(text="Апрель")
    elif month_number==5:
        result_label.config(text="Май")
    elif month_number==6:
        result_label.config(text="Июнь")
    elif month_number==7:
        result_label.config(text="Июль")
    elif month_number==8:
        result_label.config(text="Август")
    elif month_number==9:
        result_label.config(text="Сентябрь")
    elif month_number==10:
        result_label.config(text="Октябрь")
    elif month_number==11:
        result_label.config(text="Ноябрь")
    elif month_number==12:
        result_label.config(text="Декабрь")
    else:
        result_label.config(text="Неверный номер месяца")
root=tk.Tk()
root.title("Месяцы")
entry=tk.Entry(root)
entry.pack(pady=5)
show_button=tk.Button(root, text="Показать", command=month_name)
show_button.pack(pady=5)
result_label=tk.Label(root, text="", fg="black")
result_label.pack()
root.mainloop()
