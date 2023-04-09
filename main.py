import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if abs(snake.head.xcor()) > 300 or abs(snake.head.ycor()) > 280:
        scoreboard.reset_score()
        snake.reset()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_seg()
        scoreboard.update_score()
        scoreboard.show_score()

    for segment in snake.segments[1::]:
        if segment.distance(snake.head) < 10:
            scoreboard.reset_score()
            scoreboard.reset()

screen.exitonclick()
