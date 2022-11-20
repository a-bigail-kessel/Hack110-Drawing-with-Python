import turtle

turtle.bgcolor("lavender")
turtle.title("My Turtle Program")
turtle.pen(pencolor="purple", pensize =5)


turtle.forward(50)
turtle.right(90)
turtle.forward(200)

turtle.penup()
turtle.goto(100,0)
turtle.pendown()

turtle.setheading(0)

turtle.forward(50)
turtle.right(90)
turtle.forward(200)

turtle.penup()
turtle.goto(300, -180)
turtle.pendown()

turtle.setheading(0)

def oval(radius):
    turtle.left(45)
    for _ in range(2):
        turtle.circle(radius,90)
        turtle.circle(radius/2, 90)

oval(120)



turtle.done()
