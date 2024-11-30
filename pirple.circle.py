import tkinter as tk
import turtle

def draw_purple_circle():
    turtle.color("purple")
    turtle.begin_fill()
    turtle.circle(100)
    turtle.end_fill()

root = tk.Tk()
root.title("Фиолетовый круг")

canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

# Инициализация черепашки
turtle_screen = turtle.Screen()
turtle_screen.setup(width=300, height=300)
turtle_screen.tracer(0) # Отключение автоматического обновления

# Передвижение черепашки в центр экрана
turtle.penup()
turtle.goto(0, -100)
turtle.pendown()

button = tk.Button(root, text="Нарисовать круг", command=draw_purple_circle)
button.pack()

root.mainloop()
