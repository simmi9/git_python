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
    #window1.bgcolor("yellow")
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("green")
    angie.speed(2)
    angie.circle(100)
    #window1.exitonclick()

def draw_triangle():
    window3 = turtle.Screen()
    #window3.bgcolor("green") #background color
    tom = turtle.Turtle()
    tom.color("black")
    tom.speed(2)
    tom.forward(100) 
    tom.left(120)
    tom.forward(100)
    tom.left(120)
    tom.forward(100)
    window3.exitonclick() 



draw_square()
draw_circle()
draw_triangle()
