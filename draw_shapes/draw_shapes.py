import turtle
def draw_square():
    window = turtle.Screen()
    brad = turtle.Turtle()
    brad.shape( "turtle")
    brad.color("red")
    brad.speed(2)
    number = 0

    while (number != 4):
        brad.forward(100)
        brad.right(90)
        number = number + 1

    
def draw_circle():
    window1 = turtle.Screen()
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("green")
    angie.speed(2)
    angie.circle(100)
    
#window1.exitonclick()



draw_square()
draw_circle()
