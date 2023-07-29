H, W = list(map(int, input().split(' ')))
grid = []
sumW = []
for _ in range(H):
    A = list(map(int, input().split(' ')))
    sumW.append(sum(A))
    grid.append(A)

sumH = [sum([grid[h][w] for h in range(H)]) for w in range(W)]

# print(grid)
# print(sumW)
for h in range(H):
    for w in range(W):
        print(sumW[h] + sumH[w] - grid[h][w], end=' ')
    print()
