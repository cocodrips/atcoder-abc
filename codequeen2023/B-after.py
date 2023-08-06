# TLE
import collections
import heapq

N = int(input())

ng = [set() for _ in range(4)]

for i in range(N - 1):
    r, c = list(map(int, input().split(' ')))
    r -= 1
    c -= 1
    ng[0].add(r)
    ng[1].add(c)
    ng[2].add(r + c)
    ng[3].add(r - c)

for c in range(N):
    for r in range(N):
        if (r not in ng[0]
                and c not in ng[1]
                and (r + c) not in ng[2]
                and (r - c) not in ng[3]):
            print(r + 1, c + 1)
            exit()
print(-1)