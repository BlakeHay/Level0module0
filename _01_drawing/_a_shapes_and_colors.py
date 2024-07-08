import turtle


window = turtle.Screen()
window.bgcolor('white')

# This code makes a new Turtle. Pick a new name for the turtle
my_turtle = turtle.Turtle()

# Make your turtle's shape 'turtle', .shape('turtle')
my_turtle.shape('turtle')
# Set your turtle's speed using .speed(2)
my_turtle.speed(0.25)
# Set your turtle's color using .color('green') and .pencolor('blue')
my_turtle.color('green')
my_turtle.pencolor('orange')
# Move your turtle forward using .forward(100)
# TEST    Did your turtle move forward?
my_turtle.forward(150)
# Move your turtle left or right using .left(90) or .right(90)
for i in range(4):
    my_turtle.forward(70)
    my_turtle.left(90)

# Now put the forward and left/right code into a for loop to repeat 4 times.
# TEST    Did your turtle draw a square?

# Move your turtle to a new place on the screen using .goto(x, y)
# x=0 and y=0 is the center of the screen
my_turtle.goto(x = 49, y = 67)
# Have your turtle draw a circle using .circle(radius, steps=30)
# TEST    Did your turtle draw a circle?
my_turtle.begin_fill()
my_turtle.circle(37, steps=30)
my_turtle.end_fill()
# Add color to your shape by adding .begin_fill() before drawing the circle
# and .end_fill() below
my_turtle.penup()
my_turtle.goto(x = -123, y = -132)
my_turtle.pendown()
my_turtle.color('blue')


for egg in range(42):
    my_turtle.circle(43, steps=30)
    my_turtle.left(44)
    my_turtle.forward(2)

my_turtle.color('pink')
my_turtle.penup()
my_turtle.goto(x = -40, y = 60)
my_turtle.pendown()
my_turtle.begin_fill()

for a in range(5):
    my_turtle.forward(57)
    my_turtle.right(135)

my_turtle.end_fill()

my_turtle.color('yellow')
my_turtle.goto(x = -143, y = 60)
my_turtle.begin_fill()

for b in range(11):
    my_turtle.forward(34)
    my_turtle.left(60)

my_turtle.end_fill()





# Draw 3 more shapes with different fill colors!

# ===================== DO NOT EDIT THE CODE BELOW ============================
turtle.done()
