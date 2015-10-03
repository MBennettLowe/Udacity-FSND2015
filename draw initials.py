import turtle

def draw_rhombus(some_turtle):
    for i in range(1,3):
        some_turtle.forward(80)
        some_turtle.left(40)
        some_turtle.forward(80)
        some_turtle.left(140)

def draw_art(): # defind draw shapes function
    window = turtle.Screen() # set window parameters
    window.bgcolor("blue")

    #Create the turtle Brad 
    brad = turtle.Turtle()
    brad.shape("circle") # set shape builder parameters
    brad.color("gold")
    brad.width()
    brad.speed(100)

 
    for i in range(1,37):
        draw_rhombus(brad)
        brad.right(10)
    
    window.exitonclick() 

draw_art()
