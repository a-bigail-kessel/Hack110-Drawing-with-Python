import turtle

#aesthetics -- background color, title, pen color and size
turtle.bgcolor("lavender")
turtle.title("My Turtle Program")
turtle.pen(pencolor="purple", pensize =5)


#drawing the first 1
turtle.forward(50)
turtle.right(90)
turtle.forward(200)

#moving to 50p pixels over on the x-axis
turtle.penup()
turtle.goto(100,0)
turtle.pendown()

#reorienting the turtle 
turtle.setheading(0)

#drawing the second one
turtle.forward(50)
turtle.right(90)
turtle.forward(200)

#moving to draw the 0
turtle.penup()
turtle.goto(300, -180)
turtle.pendown()

#reorienting the turtle 
turtle.setheading(0)

#a function to draw the zero! yay functions
def oval(radius):
    #to account for how turtle.circle() works, drawing the oval to be sitting upright
    turtle.left(45)
    # for loop with python _ syntax and range
    for _ in range(2):
        turtle.circle(radius,90) # long part of the oval
        turtle.circle(radius/2, 90) # short top part of the oval -- can be radius over any number, 2 just looks best 

#function call to make the 0
oval(120)

#keep turtle window open --- make sure to do this at the beginning!
turtle.done()
