import tkinter as tk
root=tk.Tk()
root.title("first element")
root.geometry("200x400")
colors=["red", "orange", "yellow", "green", "blue", "indigo", "purple"]
for i, color in enumerate(colors):
    label=tk.Label(root, text=f"color {color}",bg=color, fg="white")
    label.pack(fill=tk.X,pady=5)
root.mainloop()
