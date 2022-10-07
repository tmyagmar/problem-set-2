import turtle
import math
from random import randint

while True:
    polygon = turtle.Turtle()
    lines = turtle.Turtle()
    polygon.hideturtle()
    turtle.hideturtle()
    lines.hideturtle()
    turtle.title('Regular Polygons')

# inputs(inputted side length not used for drawing)
    n = int(turtle.numinput('Shape', 'Number of sides='))
    s = int(turtle.numinput('Shape', 'Side length= '))
    s_real = 625 / n

# calculations
    angle = 360.0 / n
    area = (n * (s ** 2)) / (4 * math.tan(math.pi / n))
    perimeter = n * s
    internal_angle = (180 * (n - 2)) / n

# positioning
    r = s_real / (2 * math.sin(math.pi / n))
    polygon.penup()
    polygon.sety(r)
    polygon.right(angle / 2)
    polygon.pendown()
    lines.left(90)

# drawing
    for i in range(n):
        polygon.forward(s_real)
        polygon.right(angle)
        lines.pencolor(f'#{randint(0, 255):02x}{randint(0, 255):02x}{randint(0, 255):02x}')
        lines.forward(r)
        lines.goto(0, 0)
        lines.right(angle)

# text
    display_text = str(
        f'Num of sides = {n}\n'
        f'Side length = {s:.1f}\n'
        f'Area = {area:.2f}\n'
        f'Perimeter = {perimeter:.2f}\n'
        f'Internal Angle = {internal_angle:.2f}\n'
    )
    turtle.penup()
    turtle.goto(r + 10, -75)
    turtle.pendown()
    turtle.write(display_text, font=('Courier New', 10, 'normal'))
    turtle.color('red')
    turtle.write('Not drawn to scale', font=('Courier New', 10, 'normal'))

# redraw
    redraw = str(turtle.textinput('New Shape?', 'Enter "Y" to redraw:'))
    if redraw == 'Y':
        turtle.clearscreen()
        continue
    else:
        turtle.done()
