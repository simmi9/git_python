import turtle
def draw_square():
    window = turtle.Screen()
    
    brad = turtle.Turtle()

    brad.shape( "turtle")
    brad.color("red")
    brad.speed(2)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("green")
    angie.speed(2)
    angie.circle(100)
    
    window.exitonclick()



draw_square()
