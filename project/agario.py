import turtle
import time
import random
from ball import Ball
import math


#turtle.tracer(0,1)
turtle.hideturtle()

RUNNING=True
SLEEP=0.0077
SCREEN_WIDTH=int(turtle.getcanvas().winfo_width()/2)
SCREEN_HEIGHT=int(turtle.getcanvas().winfo_height()/2)

MY_BALL=Ball(2,2,1,1,100,"blue")

NUMBERS_OF_BALLS=6
MINIMUM_BALL_RADIUS=10
MAXIMUM_BALL_RADIUS=100
MINIMUM_BALL_DX=-5
MAXIMUM_BALL_DX=5
MINIMUM_BALL_DY=-5
MAXIMUM_BALL_DY=5

balls=[]
for i in range(NUMBERS_OF_BALLS):
    x=random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS,SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
    y=random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS)
    dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
    dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
    radius=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
    color=(random.random(), random.random(), random.random())
    ball=Ball(x,y,dx,dy,radius,color)
    balls.append(ball)


for i in balls:
    i.move(SCREEN_WIDTH,SCREEN_HEIGHT)

def collide(ball1,ball2):
    if ball1.r==ball2.r and ball1.xcor()==ball2.xcor() and ball1.ycor()==ball2.ycor():
##        print("same")
        return False
    d = math.sqrt(math.pow((ball2.xcor()-ball1.xcor()),2) + math.pow((ball2.ycor()-ball1.ycor()),2))
    if (d+10)<=ball1.r+ball2.r:
        return True
    else:
        return False

def check_collision():
    for balla in balls:
        for ballb in balls:
            if collide(balla,ballb)==True:
##                print("collide")
                if balla.r>ballb.r:
                    rad1=balla.r
                    rad1=rad1+5
                    balla.r=rad1
                    balla.shapesize(rad1/10)
                    ballb.x=random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS,SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
                    ballb.y=random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS)
                    ballb.dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
                    ballb.dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
                    ballb.radius=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
                    ballb.color(random.random(), random.random(), random.random())
                    ballb.setposition(x,y)
                    ballb.shapesize(radius/10)
                    
                elif ballb.r>balla.r:
                    rad2=ballb.r
                    rad2=rad2+5
                    ballb.r=rad2
                    ballb.shapesize(rad2/10)
                    balla.x=random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS,SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
                    balla.y=random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS)
                    balla.dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
                    balla.dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
                    balla.radius=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
                    balla.color(random.random(), random.random(), random.random())
                    balla.setposition(x,y)
                    balla.shapesize(radius/10)




check_collision()
























    
