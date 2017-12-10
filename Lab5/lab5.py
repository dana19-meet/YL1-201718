from turtle import *
colormode(255)
import random

##class Square(Turtle):
##    def __init__(self,size):
##        Turtle.__init__(self)
##        self.shapesize(size)
##        self.shape("square")
##
##    def rancolor(self):
##        r=random.randint(0,255)
##        b=random.randint(0,255)
##        g=random.randint(0,255)
##        self.color(r,b,g)
##square1=Square(7)
##square1.rancolor()

class Rect(Turtle):
    def __init__(self,width,height):
        Turtle.__init__(self)
        self.width = width
        self.height=height
        register_shape("rectangle1",((0,0),(0,height/2),(width/2,height/2),(width/2,-height/2),(-width/2,-height/2),(-width/2,height/2),(0,height/2),(0,0)))
        self.shape("rectangle1")
    def rancolor(self):
        r=random.randint(0,255)
        b=random.randint(0,255)
        g=random.randint(0,255)
        self.color(r,b,g)
##rec1=Rect(100,500)
##rec1.rancolor()

class Square(Rect):
    pass
##square1=Square(70,70)
##square1.rancolor()

class Hex(Turtle):
    def __init__(self,size):
        Turtle.__init__(self)
        self.size=size
        self.home()
        self.begin_poly()
        self.fd(size)
        self.right(60)
        self.fd(size)
        self.right(60)
        self.fd(size)
        self.right(60)
        self.fd(size)
        self.right(60)
        self.fd(size)
        self.right(60)
        self.fd(size)
        self.right(60)
        self.end_poly()
        p = self.get_poly()
        register_shape("hexa", p)

hexa1=Hex(100)










        
