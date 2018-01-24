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

turtle.color("blue")
turtle.write("eat smaller balls to get bigger. if you want to quit, just press the space bar", font = ("Ariel", 12), align="center")
time.sleep(2)
turtle.clear()

MY_BALL=Ball(2,2,1,1,30,"blue")

NUMBERS_OF_BALLS=6
MINIMUM_BALL_RADIUS=10
MAXIMUM_BALL_RADIUS=50
MINIMUM_BALL_DX=-5
MAXIMUM_BALL_DX=5
MINIMUM_BALL_DY=-5
MAXIMUM_BALL_DY=5

SPACEBAR="space"
def quitgame():
    turtle.bye()
turtle.onkeypress(quitgame,SPACEBAR)
turtle.listen()


##turtle1=turtle.Turtle()
##turtle1.hideturtle()
##turtle1.goto(0,50)
##turtle1.color("black")
##turtle1.write("eaten balls", font = ("Ariel", 12), align="left")

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
    if ball1==ball2:
        return False
    d = math.sqrt(math.pow((ball2.xcor()-ball1.xcor()),2) + math.pow((ball2.ycor()-ball1.ycor()),2))
    if (d+10)<=ball1.r+ball2.r:
        return True
    else:
        return False

##eatenballs=0
def check_collision():
    for balla in balls:
        for ballb in balls:
            if collide(balla,ballb):
                new_x = random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS,SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
                new_y = random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS)
                new_dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
                new_dy = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
                new_r = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
                new_color = (random.random(), random.random(), random.random())
                
                if balla.r>ballb.r:
                    ballb.goto(new_x, new_y)
                    ballb.dx=new_dx
                    ballb.dy=new_dy
                    ballb.r=new_r
                    ballb.color(new_color, new_color)
                    ballb.shapesize(ballb.r/10)
                    balla.r+= 10
                    balla.shapesize(balla.r/10)
##                    eatenballs+=1
                elif ballb.r>balla.r:
                    balla.goto(new_x, new_y)
                    balla.dx=new_dx
                    balla.dy=new_dy
                    balla.r=new_r
                    balla.color(new_color, new_color)
                    balla.shapesize(balla.r/10)
                    ballb.r+= 10
                    ballb.shapesize(ballb.r/10)
##                    eatenballs+=1


def check_myball_collision():
    for balla in balls:
            if collide(MY_BALL,balla)==True:
                new_x = random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS,SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
                new_y = random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS)
                if balla.r>MY_BALL.r:
                    return False
                elif MY_BALL.r>balla.r:
                    MY_BALL.r+=10
                    MY_BALL.shapesize(MY_BALL.r/10)
                    balla.goto(new_x, new_y)
                    balla.dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
                    balla.dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
                    balla.r=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
                    balla.color(random.random(), random.random(), random.random())
                    balla.shapesize(balla.r/10)
##                    eatenballs+=1
    return True

def movearound(event):
    MY_BALL.goto(event.x-SCREEN_WIDTH,SCREEN_HEIGHT-event.y)

turtle.getcanvas().bind("<Motion>",movearound)
turtle.getscreen().listen()

while RUNNING:
    if SCREEN_WIDTH!=int(turtle.getcanvas().winfo_width()/2) or SCREEN_HEIGHT!=int(turtle.getcanvas().winfo_height()/2):
        SCREEN_WIDTH=int(turtle.getcanvas().winfo_width()/2)
        SCREEN_HEIGHT=int(turtle.getcanvas().winfo_height()/2)

    
    for i in balls:
        i.move(SCREEN_WIDTH,SCREEN_HEIGHT)
    check_collision()
    MY_BALL.move(SCREEN_WIDTH,SCREEN_HEIGHT)
    RUNNING = check_myball_collision()
    turtle.getscreen().update()
    time.sleep(SLEEP)


turtle.write("Game Over", font=("Arial", 42, "normal"),align="center")
turtle.mainloop()








    
