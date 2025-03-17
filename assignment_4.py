import turtle
import random

myBrush = turtle.Turtle()
myBrush.hideturtle()
myBrush.speed(0)
width = 350
height = 350
tile_width = 100  
tile_height = 50  

def drawTile(x, y, tile_width, tile_height):  
    myBrush.penup()
    myBrush.goto(x - tile_width + randomise(), y - tile_height + randomise())
    myBrush.pendown()
    myBrush.begin_fill()
    for i in range(2): 
        myBrush.forward(tile_width - 4)
        myBrush.left(90)
        myBrush.forward(tile_height - 4)
        myBrush.left(90)
    myBrush.end_fill()

def randomise():
    return random.randint(0, 10)

def draw():
    myBrush.fillcolor("#FFB6C1")
    myBrush.color("#FFB6C1")
    for col in range(3):  
        for row in range(height // tile_height):  
            drawTile(col * (tile_width * 1.5) - 150, row * (tile_height * 1.5) - 150, tile_width * 0.95, tile_height * 0.95)

draw()
turtle.done()
