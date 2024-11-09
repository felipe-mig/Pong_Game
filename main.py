from marker import unique_marker
print(unique_marker)
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
# manage the speed
import time



screen = Screen()
screen.bgcolor("midnight blue")
# width and height in pixels
screen.setup(width=800, height=600)
# Screen title
screen.title("Ping-Pong Game")
# get rid of the animation positioning the objects at the begining of the program
''' This function is connected with the game_is_on while loop '''
screen.tracer(0)

# LEFT and RIGHT paddle positions
left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
''' We can created as many as we want using this tuple
    because we have now the Paddle class in the paddle.py. We
    just need to indicate the position'''
# top_paddle = Paddle((0, 240 ))

# BALL
ball = Ball()
# SCORE COUNT
scoreboard = Scoreboard()
    
# listeners for moving the paddels 
screen.listen()
''' REMEMBER, when using a function as a parameter, we don't add
     the parentheses, otherwise, it won't work. '''
# Move the RIGHT paddle with the up arrow and down arrow keys.    
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")
# Move the LEFT paddle up with the w key and down with s key .    
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    scoreboard.copyright()
    ''' reduce the ball speed by 0.1 sec'''
    time.sleep(ball.move_speed)
    ''' REMEMBER, that when we turn off the animation,
        we have to manually update the screen and refresh it every single time.
        After adding this function the objects will appear directly in their
        configured postion because the animation is turned off with screen.tracer(0)
        (At the top of our code)'''
    screen.update()
    ''' This function ball.move() is responsable for moving the ball'''
    ball.move()
    
    # DETECTING THE COLLISION OF THE BALL WITH THE WALL
    ''' REMEMBER, our screen is 600px height and the ball is 20px. So, 
        detecting the collision at 280px is a good number'''
    if ball.ycor() > 280 or ball.ycor() < - 280:
        # the ball needs to bounce on the walls
        ball.bounce_y()
        
    # DETECTING THE COLLISION OF THE BALL WITH THE RIGHT PADDLE
    ''' REMEMBER, our ball is 20px width and the paddle is 20px width as well
        Normally we would say, well, if that distance between the two of them is less than 20, well,
        then they've probably made contact But the problem occurs when the ball hits the paddle, 
        not right in the center, but at the edge of the paddle,
        because this distance measures the center of the ball from the centre of the
        paddle as the distance. So, we can see that this distance is way bigger than 20,
        so it's not going to register as a collision. To fix this we need to set an if conditions that 
        says if the ball has gone past a certain point on the X-axis,
        if it's gone far enough over to the right and it's within a 50 pixel distance of the paddle,
        then that also means it's made contact with the paddle '''
        
    ''' ball.distance(left_paddle) < 50 and ball.xcor() < -340
      
        This basically checks to see if the ball has gone far enough to the left as
        to be past the paddle and its within a distance of 50 pixels from the left'''
    ''' we use 320px to avoid the effect of the ball getting into the paddle when colliding.'''
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        # print("contact")
        '''When the collision is detected we are going to bounce in the X direction'''
        ball.bounce_x()
        

    # DETECTING WHEN RIGHT PADDLE MISSES THE BALL
    ''' REMEMBER, the width of the screen is 800 and we know that the paddle is at 350px.
        So, the paddle basically goes from 340px to 360px. We can say that it's already gone past 380 '''
    if ball.xcor() > 380:
        '''If the paddle misses the ball, we reset the position'''
        ball.reset_position()
        #left player scores
        scoreboard.left_point()
        
    # # DETECTING WHEN LEFT PADDLE MISSES THE BALL
    if ball.xcor() < -380:
        ball.reset_position()
        # right player scores
        scoreboard.right_point()
        
    
    
    
screen.exitonclick()



