# Import the required module
import math
from turtle import * 

# Define the functions to generate the heart shape
def hearta(k):
    return 15*math.sin(k)**3

def heartb(k):
    return 12*math.cos(k)-5*math.cos(2*k)-2*math.cos(3*k)-math.cos(4*k)

# Set the speed and background color of the turtle
speed(0)
bgcolor("black")

# Loop through a range of values to generate the heart shape
for i in range(10000): 

     # Move the turtle to the next point in the heart shape
     goto(hearta(i)*20, heartb(i)*20)

     # Set the color of the turtle to a shade of pink
     for j in range(5): 
         color("#f73487")
     
     # Move the turtle back to the center of the screen
     goto(0, 0)

# Finish drawing and exit the turtle window
done()
