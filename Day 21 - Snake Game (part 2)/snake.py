from turtle import Turtle


class Snake:
    starting_position = [(0, 0), (-20, 0), (-40, 0)]

    def __init__(self, segments_count=3):
        self.head: Turtle
        self.segments = []
        self.segments_count = segments_count
        self.__generate_snake(segments_count)

    def grow(self):
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(self.segments[-1].pos())
        self.segments.append(new_segment)

    def __generate_snake(self, segments_count: int):
        for s in range(segments_count):
            new_segment = Turtle()
            new_segment.shape("square")
            new_segment.color("white")
            new_segment.penup()
            if s != 0:
                new_segment.goto(self.segments[-1].pos())
            self.segments.append(new_segment)
        self.head = self.segments[0]

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)

    def up(self):
        position = self.head.heading()
        if position == 0:
            self.head.left(90)
        elif position == 180:
            self.head.right(90)

    def down(self):
        position = self.head.heading()
        if position == 0:
            self.head.right(90)
        elif position == 180:
            self.head.left(90)

    def right(self):
        position = self.head.heading()
        if position == 90:
            self.head.right(90)
        elif position == 270:
            self.head.left(90)

    def left(self):
        position = self.head.heading()
        if position == 90:
            self.head.left(90)
        elif position == 270:
            self.head.right(90)
