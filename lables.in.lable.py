import tkinter as tk
def find_max():
    try:
        num1=int(entry1.get())
        num2=int(entry2.get())
        num3=int(entry3.get())
        max_num=max(num1, num2, num3)
        result_label.config(text=f"max_num: {max_num}")
    except ValueError:
        result_label.config(text="error")
root=tk.Tk()
root.geometry("150x100")
entry1=tk.Entry(root)
entry1.pack(pady=5)
entry2=tk.Entry(root)
entry2.pack(pady=5)
entry3=tk.Entry(root)
entry3.pack(pady=5)
max_button=tk.Button(root, text="max_button", command=find_max)
max_button.pack(pady=5)
result_label=tk.Label(root, text="", fg="black")
result_label.pack()
root.mainloop()
