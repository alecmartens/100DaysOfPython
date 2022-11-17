from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)  # turns off animation

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_over = False
while not game_over:  # manually update the screen because turned off animations
	time.sleep(.1)
	screen.update()
	ball.move()

	# Collision with ceiling/floor
	if ball.ycor() > 280 or ball.ycor() < -280:
		ball.bounce_y()

	# Collision with paddles
	if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
		ball.bounce_x

	#Detect when right paddle misses
	if ball.xcor() > 380:
		ball.reset_position
		scoreboard.l_point()

	#Detect when left paddle misses
	if ball.xcor() < -380:
		ball.reset_position()
		scoreboard.r_point()



screen.exitonclick()
