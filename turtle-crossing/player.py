from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        # self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def go_up(self):
        y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), y)

    def at_finish_line(self):
        if self.ycor() >= 290:
            self.goto(STARTING_POSITION)
            # win
            return True
        else:
            return False
