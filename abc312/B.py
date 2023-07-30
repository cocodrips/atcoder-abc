H, W = list(map(int, input().split(' ')))
grid = []
for _ in range(H):
    S = list(input())
    grid.append(S)

black = []
white = [
    (3, 0), (3, 1), (3, 2), (3, 3), (2, 3), (1, 3), (0, 3),
    (5, 5), (5, 6), (5, 7), (5, 8), (6, 5), (7, 5), (8, 5)
]

blacks = [[0, 1, 2], [6, 7, 8]]
for b in blacks:
    for x in b:
        for y in b:
            black.append((y, x))


def check(y, x):
    for dy in range(9):
        for dx in range(9):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < W and 0 <= ny < H:
                if (dy, dx) in black:
                    if grid[ny][nx] != "#":
                        return False
                if (dy, dx) in white:
                    if grid[ny][nx] != ".":
                        return False
            else:
                return False
    return True


for y in range(H):
    for x in range(W):
        if check(y, x):
            print(y + 1, x + 1)
