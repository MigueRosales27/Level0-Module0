import turtle
from turtle import Turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # This code makes a new Turtle. Pick a new name for the turtle
    bob_turtle = turtle.Turtle()  # type: Turtle

    # Make your turtle's shape 'turtle', .shape('turtle')
    bob_turtle.shape("turtle")
    # Set your turtle's speed using .speed(2)
    bob_turtle.speed(2)
    # Set your turtle's color using .color('green') and .pencolor('blue')
    bob_turtle.color("green")
    bob_turtle.pencolor("blue")
    # Move your turtle forward using .forward(100)
    for i in range(4):
        bob_turtle.forward(100)
    # TEST    Did your turtle move forward?

    # Move your turtle left or right using .left(90) or .right(90)
        bob_turtle.left(90)
    # Now put the forward and left/right code into a for loop to repeat 4 times.
    # TEST    Did your turtle draw a square?

    # Move your turtle to a new place on the screen using .goto(x, y)
    # x=0 and y=0 is the center of the screen
    bob_turtle.goto(50, 60)
    # Have your turtle draw a circle using .circle(radius, steps=30)
    # TEST    Did your turtle draw a circle?
    bob_turtle.color("blue")
    bob_turtle.begin_fill()
    bob_turtle.circle(65, steps=30)

    # 4th shape
    bob_turtle.goto(-20, -30)
    bob_turtle.color("red")
    bob_turtle.circle(40, steps=30)

    # square
    for i in range(4):
        bob_turtle.color("purple")
        bob_turtle.left(90)
        bob_turtle.forward(120)

    bob_turtle.end_fill()

    # Add color to your shape by adding .begin_fill() before drawing the circle

    # and .end_fill() below

    # Draw 3 more shapes with different fill colors!

    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
