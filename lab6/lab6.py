from turtle import *
import random
import math

class Ball(Turtle):
    def __init__(self,radius,color,speed):
        Turtle.__init__(self)
        self.shape("circle")
        self.shapesize(radius/10)
        self.radius=radius
        self.color(color)
        self.speed(speed)
        
        
def check_collision(ball1,ball2):
    d = math.sqrt(math.pow((ball2.xcor()-ball1.xcor()),2) + math.pow((ball2.ycor()-ball1.ycor()),2))
    sumr=ball2.radius+ball1.radius
    if d < sumr:
        ball1.color("yellow")
        ball2.color("pink")
        print("they are in collision")
    elif d==sumr:
        ball1.color("yellow")
        ball2.color("pink")
        print("they are in collision")
    else:
        print("they are not in collision")

def check_collisions(ballsList):
    for ball1 in ballsList:
        for ball2 in ballsList:
            if(ball1!=ball2):
                check_collision(ball1, ball2)

ball1=Ball(10,"red",1)
ball2=Ball(20,"blue",0.5)
balls=[]
balls.append(ball1)
balls.append(ball2)




def check_collisions_v2(ballsList):
    for index1 in range(len(ballsList)):
        for index2 in range(index1, len(ballsList)):
            if(index1!=index2):  
                check_collision(ballsList[index1], ballsList[index2])

check_collisions_v2(balls)
