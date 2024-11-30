import turtle
def star(size, color):
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)
    turtle.end_fill()
turtle.speed(0)
turtle.bgcolor("black")
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
star(100, "red")
turtle.hideturtle()
turtle.done()
