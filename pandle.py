from turtle import Turtle


class Pandle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.penup()
        self.goto(position)
        self.color('white')
        self.speed('fast')
        self.shapesize(stretch_wid=7, stretch_len=1)

    def up(self):
        if self.ycor() < 390:
            new_y = self.ycor() + 50
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() > - 360:
            new_y = self.ycor() - 50
            self.goto(self.xcor(), new_y)




