# ---------------------------
# Code by Felipe Iglesias
# Created on: 2024-11-05
# ---------------------------
from turtle import Turtle

# CREATING THE PADDLE
class Paddle(Turtle):
    # Size, shape and position of the paddles
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        '''REMEMBER, all the turtles start off as 20px by 20px. So, we
            we have to stretch it by 5, and in the length, 
            we leave it as it is in order to
            make it 100px by 20px.'''
        self.shapesize(stretch_wid=5, stretch_len=1)
        ''' We want to move the position to the right of the screen. So, we
            can tell it to go to the position that is 350 X by 0 Y. We 
            remove the tracks as well with self.penup() '''
        self.penup()
        self.goto(position)
        
    # MOVING THE PADDLE
    ## methods for moving the paddel Up and Down.
    def go_up(self):
        ''' we just need a Y axis variable because the paddle will only 
            move Up and Down'''
        new_y = self.ycor() + 20
        ''' Now we can tell the paddle to go to its current paddle.xcor.
            So we're not changing that. And then to go to the new Y position. '''
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)