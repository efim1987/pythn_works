import turtle
def circles(color, x, y, radius):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
def draw_traffic_light(x, y):
    turtle.speed(0)
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("black")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(150)
        turtle.left(90)
    turtle.end_fill()
    circles("red", x+25, y+125, 20)
    circles("yellow", x+25, y+75, 20)
    circles("green", x+25, y+25, 20)
    turtle.done()
draw_traffic_light(-25, 0)
