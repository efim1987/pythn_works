import tkinter as tk 
import turtle

def act_1(radius):
    turtle.penup()
    turtle.goto(0,-radius)
    turtle.pendown()
    turtle.circle(radius)

def create_button(radius):
    button=tk.Button(root,text=f"radius {radius}",command=lambda:act_1(radius))
    button.pack()

root=tk.Tk()


canvas=tk.Canvas(root,width=300, height=300)
canvas.pack()

turtle_screen=turtle.Screen()
turtle_screen.tracer(0)
turtle.penup()
turtle.goto(0,0)
turtle.pendown()

radii=[20, 30, 40, 50, 60]
for radius in radii:
    create_button(radius)

root.mainloop()
