from turtle import Turtle as t, Screen

#Setup Screen
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.exitonclick()

#Snake Body
snake = []

head = t("square")
head.color("white")
head.goto(0, 0)
head.penup()
snake.append(head)

body = t("square")
body.color("white")
body.goto(-20, 0)
body.penup()
snake.append(body)

tail = t("square")
tail.color("white")
tail.goto(-40, 0)
tail.penup()
snake.append(tail)

# game_over = False
# while not game_over:
# 	for