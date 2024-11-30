import turtle
def squares(x, y, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)
turtle.speed(0)
turtle.bgcolor("yellow")
squares(-100, 150, 100)
squares(100, 100, 80)
squares(-150, -100, 60)
squares(-200, -200, 40)
squares(0, 0, 20)
turtle.done()
