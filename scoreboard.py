from turtle import Turtle

FONT = ("Courier", 24, "normal")
GAME_OVER_FONT = ("Courier", 54, "normal")


class Scoreboard(Turtle):
    # Write the level that we're currently on & also the GAME OVER sequence
    def __init__(self):
        super().__init__()
        self.level = 1

        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()  # prevent overwrite
        self.write(f"Level: {self.level}", align="left", font=FONT)

    # if LEVEL UP then Add 1 point to Score
    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=GAME_OVER_FONT)
