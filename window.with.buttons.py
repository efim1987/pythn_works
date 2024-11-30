import tkinter as tk

def show_definition(term):
    definitions = {
        "print": "Команда print используется в Python для вывода данных на консоль или другое устройство вывода.",
        "if": "Конструкция if используется в Python для выполнения условных операций, основанных на значении выражения.",
        "for": "Цикл for в Python используется для итерации по элементам последовательности (списку, строке и т. д.).",
        "!=": "Оператор != используется для проверки неравенства двух значений."
    }
    definition = definitions.get(term, "Такого термина нет в словаре.")
    definition_label.config(text=definition)

root = tk.Tk()
root.title("Определения терминов")
root.geometry("220x150")
root.configure(bg="blue")

print_button = tk.Button(root, text="print", command=lambda: show_definition("print"))
print_button.pack(side=tk.TOP, pady=5)

if_button = tk.Button(root, text="if", command=lambda: show_definition("if"))
if_button.pack(side=tk.TOP, pady=5)

for_button = tk.Button(root, text="for", command=lambda: show_definition("for"))
for_button.pack(side=tk.TOP, pady=5)

not_equal_button = tk.Button(root, text="!=", command=lambda: show_definition("!="))
not_equal_button.pack(side=tk.TOP, pady=5)

definition_label = tk.Label(root, text="", bg="blue", fg="white")
definition_label.pack(fill=tk.X, pady=5)

root.mainloop()
