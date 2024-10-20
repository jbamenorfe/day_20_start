# Snake class that provides template for creating snake objects

# Declare constant variables to hold the snake positions
STARTING_POSITIONS = [(0,0), (-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

from turtle import Turtle
class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]      # The head of the snake is snake_body[0]
    
    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_body_segment = Turtle(shape="square")
            new_body_segment.color("white")
            new_body_segment.penup()
            new_body_segment.setposition(position)
            self.snake_body.append(new_body_segment)
        
    def move(self):
        for body_segment in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[body_segment-1].xcor()
            new_y = self.snake_body[body_segment-1].ycor()
            self.snake_body[body_segment].goto(new_x, new_y)  
        self.head.forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)