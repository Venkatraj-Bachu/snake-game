import turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def head(self):
        return self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = turtle.Turtle('square')
        new_segment.penup()
        new_segment.color('white')
        new_segment.goto(position)
        self.segments.append(new_segment)


    def extend_snake(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for segment_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_number - 1].xcor()
            new_y = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def turn_up(self):
        self.segments[0].setheading(90)

    def turn_left(self):
        self.segments[0].setheading(180)

    def turn_down(self):
        self.segments[0].setheading(270)

    def turn_right(self):
        self.segments[0].setheading(360)
