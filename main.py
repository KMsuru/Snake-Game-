from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("Black")
screen.tracer(0)
screen.title("My Snake Game")


snake = Snake()                                # this gonna import snake class
food =  Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True                                 # we gave animation to that snake
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()                # this import move function

    # food collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # collision with segment

    for segment in snake.segments[1:]:           # here we use slicing method like we dont want to heat head so it will be 0,1,2,3,4,5 indexes thats ehyb we slice it like
                                                 # this like [1: (length of snake) : (steps we wanna skip)]
        if snake.head.distance(segment) < 10:
            game_is_on= False
            scoreboard.game_over()

    # collision with wall

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()