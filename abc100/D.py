n, m = map(int, input().split())

cakes = [[0] * n for i in range(1 << 3)]

for j in range(n):
    x, y, z = map(int, input().split())
    for i in range(1 << 3):
        s = 0
        s += x if i & (1 << 0) == 0 else -x
        s += y if i & (1 << 1) == 0 else -y
        s += z if i & (1 << 2) == 0 else -z
        cakes[i][j] = s

max_ = 0
for i in range(1 << 3):
    n = sum(sorted(cakes[i], reverse=True)[:m])
    # print(bin(i), n)
    max_ = max(max_, sum(sorted(cakes[i], reverse=True)[:m]))
print(max_)
