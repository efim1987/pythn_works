import turtle
screen=turtle.Screen()
t=turtle.Turtle()
t.speed(10)
t.color("yellow")

for _ in range(36):
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.forward(100)
    t.penup()
    t.goto(0,0)
    t.left(10)
turtle.done()