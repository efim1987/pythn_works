import tkinter as tk
import turtle

def draw_triangle():
    triangle_screen = turtle.Screen()
    triangle_screen.setup(width=300, height=300)
    turtle_triangle = turtle.Turtle()
    turtle_triangle.penup()
    turtle_triangle.goto(-50, -100)
    turtle_triangle.pendown()
    turtle_triangle.color("yellow")
    turtle_triangle.begin_fill()
    for _ in range(3):
        turtle_triangle.forward(100)
        turtle_triangle.left(120)
    turtle_triangle.end_fill()
    triangle_screen.mainloop()

def draw_square():
    square_screen = turtle.Screen()
    square_screen.setup(width=300, height=300)
    turtle_square = turtle.Turtle()
    turtle_square.penup()
    turtle_square.goto(-50, -100)
    turtle_square.pendown()
    turtle_square.color("red")
    turtle_square.begin_fill()
    for _ in range(4):
        turtle_square.forward(100)
        turtle_square.left(90)
    turtle_square.end_fill()
    square_screen.mainloop()

def draw_circle():
    circle_screen = turtle.Screen()
    circle_screen.setup(width=300, height=300)
    turtle_circle = turtle.Turtle()
    turtle_circle.penup()
    turtle_circle.goto(-50, -100)
    turtle_circle.pendown()
    turtle_circle.color("blue")
    turtle_circle.begin_fill()
    turtle_circle.circle(50)
    turtle_circle.end_fill()
    circle_screen.mainloop()

root = tk.Tk()
root.title("Фигуры")

triangle_button = tk.Button(root, text="Треугольник", command=draw_triangle)
triangle_button.pack(side=tk.LEFT)

square_button = tk.Button(root, text="Квадрат", command=draw_square)
square_button.pack(side=tk.LEFT)

circle_button = tk.Button(root, text="Круг", command=draw_circle)
circle_button.pack(side=tk.LEFT)

root.mainloop()
