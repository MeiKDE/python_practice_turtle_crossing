from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280  # finish line coordinate


class Player(Turtle):

    # Turtle can only move forward by pressing "Up" key.
    def __init__(self):
        super().__init__()
        self.color("pink")
        self.shape("turtle")
        self.penup()  # stop drawing
        self.go_to_start()
        self.setheading(90)  # faces north

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    # When turtle hits the top edge of the screen, it moves back to the original position and the player levels up.  On the next level, the car speed increases.
    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
