from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.increment = 1

    def level(self):
        self.clear()
        self.penup()
        self.color("black")
        self.goto(-240, 260)
        self.write(f"Level: {self.increment}", font=FONT)

    def increase_level(self):
        self.increment += 1


class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()

    def write_over(self):
        self.hideturtle()
        self.penup()
        self.goto(-100, 0)
        self.color("black")
        self.write("Game Over", font=FONT)



