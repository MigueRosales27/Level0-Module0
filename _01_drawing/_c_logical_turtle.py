import random
import turtle


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))

# ====================== DO NOT EDIT THE CODE ABOVE ===========================


def screen_clicked(x, y):
    print('You pressed: x=' + str(x) + ', y=' + str(y))
    
    # 6. Call the turtle .penup() method

    johnny_turtle.penup()

    # 7. Move the turtle to a new location using .goto(x, y)

    johnny_turtle.goto(50,50)

def turtle_clicked(x, y):
    print('turtle clicked!')
    
    # 8. Make a for loop to run the next instructions 3 times

    for i in range (3):

        # 9. Make the turtle spin 360 degrees using the .right() method

        johnny_turtle.right(360)

        # 10. Use the .color() method and getRandomColor() function to change

        johnny_turtle.color(get_random_color())

        # the color of the turtle,
        # myTurtle.color(get_random_color())


if __name__ == '__main__':
    window = turtle.Screen()
    window.setup(width=0.75, height=0.8, startx=0, starty=0)
    
    # 1. Make a new turtle
    johnny_turtle = turtle.Turtle()
    # 2. Make your turtle's shape 'turtle', .shape('turtle')
    johnny_turtle.shape('turtle')
    # 3. Set your turtle's color using .color('green') and .pencolor('blue')
    johnny_turtle.color('green')
    johnny_turtle.pencolor('blue')
    # 4. Set and new width, length, and outline of our turtle
    #    my_turtle.turtlesize(stretch_wid=10, stretch_len=10, outline=4)

    johnny_turtle.turtlesize(10 , 10 , 4)

    # 5. Uncomment the following line and replace 'my_turtle' with your turtle
    # my_turtle.onclick(turtle_clicked)

    johnny_turtle.onclick(turtle_clicked)

# ===================== DO NOT EDIT THE CODE BELOW ============================
    window.onclick(screen_clicked)
    turtle.done()
