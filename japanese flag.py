import turtle
def draw_circle(color, x, y, widht, height):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(widht)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()
def draw_flag():
    turtle.speed(0)
    turtle.bgcolor("green")
    turtle.penup()
    turtle.goto(100, -100)
    turtle.pendown()
    draw_circle("white", 0, 0, -200, 130)
    turtle.color("red")
    turtle.penup()
    turtle.goto(-100, -100)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(40)
    turtle.end_fill()
    turtle.done()
draw_flag()
