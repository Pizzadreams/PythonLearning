from turtle import Turtle

FONT = ("Courier", 24, "normal")

class PauseMenu(Turtle):
    def __init__(self):
        super().__init__()
        self.is_paused = False
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(0, 0)

    def toggle_pause(self):
        self.is_paused = not self.is_paused
        self.clear()
        return self.is_paused

    # def toggle_resume(self):
    #     self.is_paused = not self.is_paused
    #     return self.is_paused

    def display(self):
        self.goto(0, 0)
        self.clear()
        self.write("Game Paused", align="center", font=FONT)
