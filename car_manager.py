from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager():
    def __init__(self):
        self.starting_speed = 5
        self.increment = 10
        self.all_turtles = []

    def make_car(self):
        random_chance = random.randint(0,6)
        if random_chance == 1 or random_chance == 2:
            new_turtle = Turtle("square")
            new_turtle.shapesize(stretch_wid=0.8, stretch_len=2)
            new_turtle.penup()
            new_turtle.color(random.choice(COLORS))
            new_turtle.goto(300, random.randint(-250, 250))
            new_turtle.setheading(180)
            self.all_turtles.append(new_turtle)

    def move(self):
        for turtles in self.all_turtles:
            if turtles.xcor() < -280:
                turtles.goto(300, random.randint(-250, 250))
            else:
                turtles.forward(self.starting_speed)

    def increase_speed(self):
        self.starting_speed += self.increment

