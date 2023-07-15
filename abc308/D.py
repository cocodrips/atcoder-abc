H, W = map(int, input().split(' '))
v = []
for i in range(H):
    line = input()
    v.append(list(line))

s = "snuke"


def main():
    candidate = [(0, 0)]
    visited = set()
    char_map = [[s.find(x) for x in line] for line in v]
    while candidate:
        y, x = candidate.pop()
        if y == H - 1 and x == W - 1:
            return True
        for y1, x1 in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            yy = y + y1
            xx = x + x1
            if (
                    0 <= yy < H
                    and 0 <= xx < W
                    and (yy, xx) not in visited
                    and char_map[yy][xx] == (char_map[y][x] + 1) % 5):
                candidate.append((yy, xx))
                visited |= {(yy, xx)}
                # print(candidate)
    return False


if main():
    print('Yes')
else:
    print('No')
