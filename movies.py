import turtle

def draw_square(some_turtle):
    for i in range(1,5):
         some_turtle.forward(100)
         some_turtle.right(90)
def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    #create the turtle Brad - draw a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("black")
    brad.speed(2)
    draw_square(brad)
    #create the turtle Angie- draw a circle
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

    window.exitonclick()
draw_art();
