from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    # Create cars that are 20px high by 40px wide
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        # Generate a new car only every 6th time the game loop runs.
        random_chance = random.randint(1, 6)
        if random_chance == 1:  # want to slow down the random cars being created.
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)  # default is 20 by 20
            new_car.penup()
            new_car.color(random.choice(COLORS))
            # No cars should be generated in the top and bottom 50px of the screen
            random_y = random.randint(-250, 250)
            # want to create a car at different y position
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    # Random generate cars along the y-axis (up and down) and will move from the right edge of screen to the left edge
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    # Level up
    def level_up(self):
        self.car_speed += MOVE_INCREMENT
