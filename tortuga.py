"""
	This code moves the turtle to a vertex of the polygon
	to center the drawing of the figure.
"""

import turtle as T
import math as M
import sys

if len(sys.argv) < 4:
	print("Run this file like this:")
	print("\tpy tortuga.py NUM_SIDES SIDES_LENGTH TIME_BY_STEP")
	exit(1)

sides = int(sys.argv[1])
length = int(sys.argv[2])
time_by_step = int(sys.argv[3])

if sides <= 2:
	print("You cannot give a number of sides less than or equal to two.")
	exit(1)

if length <= 0:
	print("You cannot give a length less than or equal to zero.")
	exit(1)

if not 0 <= time_by_step <= 10:
	print("You cannot give a time out of [0,10] range.")
	exit(1)

step = 360/sides
alpha = (180-step)/2

# Mathemagics!
radians = M.radians(alpha)
radius = length/(M.cos(radians)*2)
init_pos_x = radius*M.cos(radians)
init_pos_y = radius*M.sin(radians)

T.shape("turtle")
T.color("white","gray")
T.bgcolor("black")
T.speed(2)

T.penup()
T.goto(-init_pos_x,-init_pos_y)
T.pendown()

T.speed(time_by_step)

T.begin_fill()

for _ in range(sides):
	T.forward(length)
	T.left(step)

T.end_fill()

T.mainloop()
