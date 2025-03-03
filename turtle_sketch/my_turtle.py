import random
import math
from turtle import *

title("my first sketch")
shape("turtle")
speed(2)
pensize(2)
colormode(255)
speed(0)
bgcolor("lightblue")
pencolor("pink")

colors=["pink", "#FA8072", "#DFFF00", "#CCCCFF", "#800080", "#FF4500"]

def draw_flower(x, y):
    penup()
    goto(x, -300)
    pendown()
    color("green")
    goto((x, y))
    #fillcolor("pink")
    color(random.choice(colors))
    begin_fill()
    for i in range(5):
        circle(20)
        left(360/5)
    end_fill()
onscreenclick(draw_flower)


mainloop()
#one hexagon:
# for i in range(6):
#     forward(100)
#     left(60) 

#many hexagons in lots of colors, random: 

# colors= ["red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan"]

# for n in range(36):
#     color(random.choice(colors))
#     c=colors[n%8]
#     color(c)
#     #fillcolor(c)
#     #begin_fill()
#     for i in range(6):
#         forward(100)
#         left(60)
#     #end_fill()
#     left(10) 

# mainloop()

#pencolor("yellow")

#colors = ['blue', 'red', 'green'] 

# count = 5
# angle = 360 / count
# size = 100

# for i in range(count):
#     left(angle)
#     circle(size - i*10) #same as size=size-10)

# count = 5
# angle = 360 / count
# size = 100

# # for i in range(count):
# #     left(angle)
# #     for j in range(count):
# #         circle(size - j * 10)

# pencolor("red")
# pensize(2)

# for i in range(6):
#     left(360/6) #divided by number of petals
#     for j in range(count): #inner loop is different sizes
#         circle(size/2 + j * 5)

# pencolor("pink")
# for i in range(3):
#     left(360/3)
#     for j in range(count):
#         circle(size/3 + j * 5) 

# penup()
# goto(200, 200)
# pendown()

# pencolor("red")
# pensize(2)

# for i in range(6):
#     left(360/6) #divided by number of petals
#     for j in range(count): #inner loop is different sizes
#         circle(size/2 + j * 5)

# pencolor("pink")
# for i in range(3):
#     left(360/3)
#     for j in range(count):
#         circle(size/3 + j * 5) 

# penup()
# goto(100, 100)
# pendown()

# pencolor("red")
# pensize(2)

# for i in range(6):
#     left(360/6) #divided by number of petals
#     for j in range(count): #inner loop is different sizes
#         circle(size/2 + j * 5)

# pencolor("pink")
# for i in range(3):
#     left(360/3)
#     for j in range(count):
#         circle(size/3 + j * 5) 

# penup()
# goto(-100, -100)
# pendown()


# pencolor("red")
# pensize(2)

# for i in range(6):
#     left(360/6) #divided by number of petals
#     for j in range(count): #inner loop is different sizes
#         circle(size/2 + j * 5)

# pencolor("pink")
# for i in range(3):
#     left(360/3)
#     for j in range(count):
#         circle(size/3 + j * 5) 

# penup()
# goto(-200, -200)
# pendown()

# pencolor("red")
# pensize(2)

# for i in range(6):
#     left(360/6) #divided by number of petals
#     for j in range(count): #inner loop is different sizes
#         circle(size/2 + j * 5)

# pencolor("pink")
# for i in range(3):
#     left(360/3)
#     for j in range(count):
#         circle(size/3 + j * 5)

# mainloop()

# colors = ['blue', 'red', 'green'] 

# # for i in range(100):   
# #     forward(100)
# #     right(170) 

# speed(0)
# color("red")
# fillcolor("yellow")

# begin_fill()
# while True:
#     forward(200)
#     left(170) # change a different angle value
#     if abs(pos()) < 1: # use `abs(pos()) < 1` to determine if turtle is back at it home position
#         break
# end_fill()

# mainloop()



# title("my first sketch")
# shape("turtle")
# speed(2)
# pensize(2)
# colormode(255)
# bgcolor("lightblue")
# pencolor("yellow")



# fillcolor("red") 

# def draw_square():
#     for i in range(4):
#         forward(100)
#         left(90)

# # begin_fill() 
# # forward(100)
# # left(90)
# # forward(100)
# # left(90)
# # forward(100)
# # left(90)
# # forward(100)
# # left(90)
# # end_fill() 

# begin_fill()
# draw_square()
# end_fill()

# penup()
# forward(110)
# pendown()

# pencolor("blue")
# fillcolor("pink")

# begin_fill()
# draw_square()
# end_fill()


# penup()
# goto(200,200)
# pendown()

# begin_fill()
# circle(100)
# end_fill()



# mainloop()


