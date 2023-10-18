import time
import turtle
import snake
import food
import scoreboard


screen = turtle.Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = snake.Snake()
food = food.Food()
scoreboard = scoreboard.Scoreboard()
scoreboard.update_screen()

screen.listen()
screen.onkey(snake.turn_left, 'Left')
screen.onkey(snake.turn_right, 'Right')
screen.onkey(snake.turn_up, 'Up')
screen.onkey(snake.turn_down, 'Down')

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head().distance(food) < 15:
        scoreboard.score+=1
        scoreboard.update_screen()
        food.refresh()
        snake.extend_snake()

    #Detect collision with wall
    if snake.head().xcor() > 270 or snake.head().xcor() < -270:
        scoreboard.reset()
        snake.reset()
    elif snake.head().ycor() > 270 or snake.head().ycor() < -270:
        scoreboard.reset()
        snake.reset()

    #Detect collision with own tail
    for segment in snake.segments[1:]:
        if snake.head().distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
