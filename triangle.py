import turtle

screen=turtle.Screen()
t=turtle.Turtle()

t.penup()
t.goto(-100,-100)
t.pendown()
t.color("red")
for _ in range(3):
    t.forward(200)
    t.left(120)

t.penup()
t.goto(0,0)
t.pendown()
t.color("green")
for _ in range(3):
    t.forward(200)
    t.left(120)

t.penup()
t.goto(100,-100)
t.pendown()
t.color("yellow")
for _ in range(3):
    t.forward(200)
    t.left(120)

turtle.done()
