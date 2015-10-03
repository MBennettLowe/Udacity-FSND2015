import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art(): # defind draw shapes function
    window = turtle.Screen() # set window parameters
    window.bgcolor("grey")

    #Create the turtle Brad - draw a square
    brad = turtle.Turtle()
    brad.shape("circle") # set shape builder parameters
    brad.color("green")
    brad.width()
    brad.speed(2)

    for i in range(4): # used a for loop to create square shape
        brad.forward(100)
        brad.right(90)

    for i in range(1,36):
        draw_square(brad)
        brad.right(10)
    
##    angie = turtle.Turtle() # second instance of turtle creating a circle
##    angie.width()   # setting the circle parameters
##    angie.shape("arrow") 
##    angie.color("blue")
##    angie.circle(100) # draw a circle 100 degrees
##
##    celina = turtle.Turtle() # third instance of turtle creating a triangle
##    celina.width(6)     # setting the triangle parameters
##    celina.shape("turtle")
##    celina.color("yellow")
##    for i in range(0,3):
##        celina.forward(100)
##        celina.left(180-60)

    window.exitonclick() 

draw_art()
