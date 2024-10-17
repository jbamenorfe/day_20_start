# Snake class that provides template for creating snake objects
from turtle import Turtle
class Snake:
    def __init__(self):
        self.snake_body_segment_positions = [(0,0), (-20,0),(-40,0)]
        self.snake_body = []

        for position in self.snake_body_segment_positions:
            new_body_segment = Turtle(shape="square")
            new_body_segment.color("white")
            new_body_segment.penup()
            new_body_segment.setposition(position)
            self.snake_body.append(new_body_segment)
        
    def move(self):
        for body_segment in range(len(self.snake_body)-1, 0, -1):
            new_x = self.snake_body[body_segment-1].xcor()
            new_y = self.snake_body[body_segment-1].ycor()
            self.snake_body[body_segment].goto(new_x, new_y)  
        self.snake_body[0].forward(20)
