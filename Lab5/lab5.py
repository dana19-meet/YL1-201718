##from turtle import *
##class Square(Turtle):
##    def __init__(self,size,color):
##        Turtle.__init__(self)
##        self.shapesize(size)
##        self.color(color)
##        self.shape("square")
##
##square1=Square(7,"red")

class Rectangle(Turtle):
    def __init__(self,width,height):
        Turtle.__init__(self)
        turtle.width(width)
        turtle.height(height)
        register_shape("rectangle1",(0,0),(0,height/2),(width/2,height/2),(width/2,-height/2),(-width/2,-height/2),(-width/2,height/2),(0,height/2),(0,0)
rec=Rectangle(50,10)
