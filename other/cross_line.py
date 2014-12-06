class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def is_cross(self, other):
        if (((self.start.x - self.end.x) * (other.start.y - self.start.y)
            + (self.start.y - self.end.y) * (self.start.x - other.start.x))
            * ((self.start.x - self.end.x) * (other.end.y - self.start.y)
            + (self.start.y - self.end.y) * (self.start.x - other.end.x)) < 0):

            if (((other.start.x - other.end.x) * (self.start.y - other.start.y)
                + (other.start.y - other.end.y) * (other.start.x - self.start.x))
                * ((other.start.x - other.end.x) * (self.end.y - other.start.y)
                + (other.start.y - other.end.y) * (other.start.x - self.end.x)) < 0):
                return True
        return False

