from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0) ]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:  # we created snake
            self.add_segment(position)

    def add_segment(self, position):
        newSegment = Turtle("square")
        newSegment.color("white")
        newSegment.penup()
        newSegment.goto(position)
        self.segments.append(newSegment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # here we can see that len(segment) this means "start" like snake can be of any length
            # 0 means "stop"
            # -1 means "steps" snake move with -1
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)  # hence it will move depends on it
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)