class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def cross(p1, p2, p3, p4):
    if (((p1.x - p2.x) * (p3.y - p1.y) + (p1.y - p2.y) * (p1.x - p3.x)) *
        ((p1.x - p2.x) * (p4.y - p1.y) + (p1.y - p2.y) * (p1.x - p4.x)) < 0):
        if (((p3.x - p4.x) * (p1.y - p3.y) + (p3.y - p4.y) * (p3.x - p1.x)) *
            ((p3.x - p4.x) * (p2.y - p3.y) + (p3.y - p4.y) * (p3.x - p2.x)) < 0):
            return True
    return False


if __name__ == "__main__":
    x1,y1,x2,y2 = map(int, raw_input().split())
    base1 = Point(x1,y1)
    base2 = Point(x2, y2)

    n = int(raw_input())
    points = []
    for i in xrange(n):
        x, y = map(int, raw_input().split())
        points.append(Point(x,y))

    cross_count = 0
    for i in xrange(n):
        if cross(points[i], points[(i + 1) % n], base1, base2):
            cross_count += 1

    print  1 + cross_count / 2
