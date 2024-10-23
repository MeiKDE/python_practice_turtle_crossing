import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FONT = ("Courier", 45, "normal")

# Setting up the screen properties
screen = Screen()

screen.setup(width=600, height=600)
screen.title("My Turtle Crossing Game")
screen.tracer(0)  # turn off animation

player = Player()  # create turtle player
car_manager = CarManager()  # create random cars
scoreboard = Scoreboard()  # calculate score and level

# player movement using UP key
screen.listen()
player.go_to_start()
screen.onkey(key="Up", fun=player.go_up)


game_is_on = True
# Loop while game is on
while game_is_on:
    time.sleep(0.1)  # refreshed every xx second
    screen.update()  # show screen after bypassing animation
    # create many cars
    car_manager.create_car()
    # move cars backward at a certain speed
    car_manager.move_cars()

    # Detect collision within list of cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:  # car distance against turtle player
            game_is_on = False  # Game Over
            scoreboard.game_over()

    # Detect a successful crossing
    if player.is_at_finish_line():
        player.go_to_start()  # starting position
        car_manager.level_up()  # increase speed
        scoreboard.increase_level()  # increase score

screen.exitonclick()
