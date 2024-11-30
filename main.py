import turtle

screen=turtle.Screen()
t=turtle.Turtle()

t.width(10)
t.speed(6)

t.penup()
t.goto(-110,0)
t.pendown()
t.color("blue")
t.circle(100)

t.penup()
t.goto(0,0)
t.pendown()
t.color("yellow")
t.circle(100)

t.penup()
t.goto(110,0)
t.pendown()
t.color("black")
t.circle(100)

t.penup()
t.goto(-55,-100)
t.pendown()
t.color("green")
t.circle(100)

t.penup()
t.goto(55,-100)
t.pendown()
t.color("red")
t.circle(100)

turtle.done()
