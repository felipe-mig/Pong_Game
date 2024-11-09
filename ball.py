from turtle import Turtle

# CREATING THE BALL
class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("orange")
        self.shape("circle")
        self.penup()
        # setting the bouncing
        ''' every single time the ball moves,
            it's going to increase in the X coordinate by 10 pixels
            and also increased by 10 pixels in the Y coordinate. '''
        self.x_move = 10
        self.y_move = 10
        # increase the speed of the ball
        self.move_speed = 0.080
        
    ## Moving the ball
    def move(self):
        '''we are going to move the ball by increasing on the X and Y'''
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        
    ## Method to bounce the ball in the Y axis
    def bounce_y(self):
        '''For bouncig the Y coordinate needs to reverse it. So, instead of
            increasing +10px we need to decrease it. We do it by multiplying it by -1
            in this way we have -10px'''
        self.y_move *= -1       
        
    # Method to bounce the ball on the X axis
    def bounce_x(self):
        self.x_move *= -1
        # increase the ball speed each time the ball touches the paddle
        self.move_speed *= 0.9
        
    # Method to reset the position of the ball when the paddle misses the collision
    def reset_position(self):
        self.goto(0, 0)
        '''restart the ball speed so it doesn't increase indefinitely '''
        self.move_speed = 0.1
        ''' this will send the ball to the opposite direction when reset '''
        self.bounce_x()
        

        