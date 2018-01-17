from turtle import Turtle
class Ball(Turtle):
    def __init__(self,x,y,dx,dy,r,color):
        Turtle.__init__(self)
        self.penup()
        self.x=x
        self.y=y
        self.setposition(x,y)
        self.dx=dx
        self.dy=dy
        self.shape("circle")
        self.r=r
        self.shapesize(r/10)
        self.color(color)

        
    def move(self,screen_width,screen_height):

        current_x=self.xcor()
        new_x=current_x+self.dx
        current_y=self.ycor()
        new_y=current_y+self.dy
        right_side_ball=new_x+self.r
        left_side_ball=new_x-self.r
        up_side_ball=new_y+self.r
        down_side_ball=new_y-self.r
        self.goto(new_x,new_y)
        if right_side_ball>=(screen_width/2):
            new_x=new_x-self.dx
        elif left_side_ball<=(screen_width/2):
            new_x=new_x+self.dx
        elif up_side_ball<=(screen_height/2):
            new_y=new_y-self.dx
        elif down_side_ball<=(screen_height/2):
            new_y=new_y+self.dx

ball1=Ball(0,0,1,1,100,"blue")
