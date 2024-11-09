from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()
        # copyright?
   
        
    def update_scoreboard(self):
        # Left side player
        ''' Prevent overwriting '''
        self.clear()
        ''' postion on screen of the score'''
        self.goto(-100, 190)
        self.write(self.left_score, align="center",  font=("Courier", 80, "normal"))
        # Right side player score
        self.goto(100, 190)
        self.write(self.right_score, align="center",  font=("Courier", 80, "normal"))
        
        
    # Increase the points of the left side player
    def left_point(self):
        self.left_score += 1
        self.update_scoreboard()
        
    # Increase the points of the right side player
    def right_point(self):
        self.right_score += 1
        self.update_scoreboard()
        
    #copyright
    def copyright(self):
        self.color("azure")
        self.goto(0, -287)
        self.write("© Felipe Iglesias", align="center",  font=("Courier", 12, "normal"))
        self.color("white")