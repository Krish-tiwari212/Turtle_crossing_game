from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()

    def make_player(self):
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def up(self):
        if self.ycor() > 265:
            pass
        else:
            self.forward(MOVE_DISTANCE)

    def down(self):
        if self.ycor() < -265:
            pass
        else:
            self.backward(MOVE_DISTANCE)



