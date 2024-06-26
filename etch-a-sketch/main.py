from turtle import Turtle, Screen

t = Turtle()
screen = Screen()

def move_forwards():
    t.forward(10)

def turn_left():
    t.left(10)
    # t.setheading(t.heading() + float(10))

def move_backwards():
    t.back(10)

def turn_right():
    t.right(10)
    # t.setheading(t.heading() - float(10))

def clear():
    t.penup()
    t.clear()
    t.home()
    t.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)


screen.exitonclick()
