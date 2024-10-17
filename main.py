from turtle import Screen
from snake import Snake
import time

# Create a new Screen
screen = Screen()

# Set up the screen to be 600px by 600px
screen.setup(width=600, height=600)

# Set the screen's background color
screen.bgcolor("black")

# Set the title of the game
screen.title("My Snake Game")

# Set the tracer property of the screen object to zero. This ensures that all snake body segments are drawn before they are displayed on the screen
screen.tracer(0)

# TODO 1: Create the Snake Body
snake = Snake()

# TODO 2: Move the snake on the screen
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()

    screen.listen()         # Listen to key press events
    screen.onkey(fun=snake.right, key="Right")
    screen.onkey(fun=snake.up, key="Up")
    screen.onkey(fun=snake.left, key="Left")
    screen.onkey(fun=snake.down, key="Down")






# Set the screen to disappear only when it is clicked
screen.exitonclick()
