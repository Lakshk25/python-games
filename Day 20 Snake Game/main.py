from turtle import Screen
from food import Food
import time
from snake import Snake
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600 , height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()
game_on = True

screen.onkey(snake.up , "Up")
screen.onkey(snake.down , "Down")
screen.onkey(snake.left , "Left")
screen.onkey(snake.right , "Right")
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
    
    # detect collision with wall

    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285 :
        # score.game_over()
        # game_on = False
        score.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            # game_on = False
            # score.game_over()
            score.reset()
            snake.reset()

screen.exitonclick()