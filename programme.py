import tkinter as tk
import turtle
import time

# Функция для рисования прямоугольника
def draw_rectangle():
    turtle.clear()  # Очищаем экран перед рисованием новой фигуры
    turtle.color("red")
    turtle_screen.update()  # Обновляем экран
    time.sleep(0.1)  # Даем небольшую задержку
    for _ in range(2):
        turtle.forward(100)  # Длина
        turtle.right(90)
        turtle.forward(50)   # Ширина
        turtle.right(90)

# Функция для рисования треугольника
def draw_triangle():
    turtle.clear()  # Очищаем экран перед рисованием новой фигуры
    turtle.color("green")
    turtle_screen.update()  # Обновляем экран
    time.sleep(0.1)  # Даем небольшую задержку
    for _ in range(3):
        turtle.forward(100)
        turtle.right(120)

# Функция для рисования круга
def draw_circle():
    turtle.clear()  # Очищаем экран перед рисованием новой фигуры
    turtle.color("blue")
    turtle_screen.update()  # Обновляем экран
    time.sleep(0.1)  # Даем небольшую задержку
    turtle.circle(50)

# Создаем главное окно
root = tk.Tk()
root.title("Рисование фигур")

# Создаем виджеты кнопок
rectangle_button = tk.Button(root, text="Прямоугольник", command=draw_rectangle)
rectangle_button.pack(side=tk.LEFT, padx=5, pady=5)

triangle_button = tk.Button(root, text="Треугольник", command=draw_triangle)
triangle_button.pack(side=tk.LEFT, padx=5, pady=5)

circle_button = tk.Button(root, text="Круг", command=draw_circle)
circle_button.pack(side=tk.LEFT, padx=5, pady=5)

# Инициализируем черепашку
turtle_screen = turtle.Screen()
turtle_screen.setup(width=400, height=400)
turtle_screen.tracer(0, 0)
turtle_screen.listen()

turtle.penup()
turtle.hideturtle()

# Запускаем главный цикл обработки событий
root.mainloop()
