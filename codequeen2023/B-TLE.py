# TLE
import collections
import heapq

N = int(input())
table = [[False for i in range(N)] for _ in range(N)]
for i in range(N - 1):
    r, c = list(map(int, input().split(' ')))
    table[r - 1][c - 1] = True

# 先に計算
tate = [False] * N
yoko = [False] * N
naname = [False] * 2 * N
naname2 = [False] * 2 * N

# yoko
for i in range(N):
    yoko[i] = any(table[i])

# 縦, naname
for c in range(N):
    for r in range(N):
        tate[c] |= table[r][c]
        naname[r + (N - c)] |= table[r][c]
        naname2[r + c] |= table[r][c]

for c in range(N):
    for r in range(N):
        if (not yoko[r]
                and not tate[c]
                and not naname[r + (N - c)]
                and not naname2[r + c]):
            print(r + 1, c + 1)
            exit()
print(-1)