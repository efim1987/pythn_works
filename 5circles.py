import turtle
def circles(x, y, radius):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(radius)
turtle.speed(0)
turtle.bgcolor("white")
circles(-360, 360, 60)
circles(-300, 300, 50)
circles(-240, 240, 40)
circles(-180, 180, 30)
circles(-120, 120, 20)
turtle.done()
