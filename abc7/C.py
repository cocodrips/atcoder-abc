import Queue


class Axis(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class M(object):
    def __init__(self, n, axis):
        self.n = n
        self.axis = axis

    @property
    def x(self):
        return self.axis.x

    @property
    def y(self):
        return self.axis.y


def solve(maze, start_y, start_x, goal_y, goal_x):
    direction = ((1, 0), (-1, 0), (0, 1), (0, -1))
    goal = Axis(goal_x - 1, goal_y - 1)
    start = Axis(start_x - 1, start_y - 1)

    queue = Queue.Queue()
    queue.put(M(0, start))

    while not queue.empty():
        q = queue.get()

        if q.axis == goal:
            return q.n

        for d in direction:
            axis = Axis(q.x + d[0], q.y + d[1])
            if maze[axis.y][axis.x] == '.':
                maze[axis.y][axis.x] = str(q.n + 1)
                queue.put(M(q.n + 1, axis))

    return -1


if __name__ == "__main__":
    R, C = map(int, raw_input().split())
    sy, sx = map(int, raw_input().split())
    gy, gx = map(int, raw_input().split())

    maze = []
    for i in xrange(R):
        maze.append(list(raw_input()))
    print solve(maze, sy, sx, gy, gx)
