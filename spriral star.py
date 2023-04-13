# Importing required libraries
from turtle import *
import colorsys

# Set turtle speed to maximum, set background color to black, initialize hue and hide turtle
speed(0)
bgcolor('black')
hue=0.0
hideturtle()
pensize(3)

# Loop 400 times to create spiral
for i in range (400):
    # Convert hue value to RGB using colorsys library, set pen color
    color=colorsys.hsv_to_rgb(hue,1,1)
    pencolor(color)
    
    # Move turtle forward by i units, turn right by 98 degrees
    fd(i)
    rt(98)
    
    # Increment hue value by 0.005
    hue+=0.005
    
# End turtle graphics
done()
