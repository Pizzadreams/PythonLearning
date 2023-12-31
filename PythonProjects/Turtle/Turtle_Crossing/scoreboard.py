from turtle import Turtle

FONT = ("Courier", 24, "normal")
GAME_OVER_FONT = ("Courier", 40, "normal")
ALIGNMENT = "left"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.setposition(-280, 250)
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

