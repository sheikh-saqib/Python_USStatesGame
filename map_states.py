from turtle import Turtle


class Map_States(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def update_map(self, state):
        self.goto(int(state.x), int(state.y))
        self.write(str(state.state.item()), align="center", font=("Courier", 8, "normal"))
