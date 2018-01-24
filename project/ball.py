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

        if right_side_ball>=screen_width:
            self.dx=-self.dx
            new_x = current_x
        elif left_side_ball<=-screen_width:
            self.dx=-self.dx
            new_x = current_x
        elif up_side_ball>=screen_height:
            self.dy=-self.dy
            new_y = current_y
        elif down_side_ball<=-screen_height:
            self.dy=-self.dy
            new_y = current_y

        self.goto(new_x,new_y)
        
