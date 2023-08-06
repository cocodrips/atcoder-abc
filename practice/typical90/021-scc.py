import collections
import heapq
# N = int(input())
# list(map(int, input().split(' ')))
import sys
sys.setrecursionlimit(1000000 + 10)

used= [False] * (1 << 18)
G = [[] for _ in range(1 << 18)]
H = [[] for _ in range(1 << 18)]
I = []
cnts = 0

def dfs(pos):
    used[pos] = True
    for i in G[pos]:
        if not used[i]:
            dfs(i)
    I.append(pos)

def dfs2(pos):
    global cnts
    used[pos] = True
    cnts += 1
    for i in H[pos]:
        if not used[i]:
            dfs2(i)

N, M = map(int, input().split(' '))
for i in range(M):
    A, B = map(int, input().split(' '))
    G[A].append(B)
    H[B].append(A)

for i in range(1, N + 1):
    if not used[i]:
        dfs(i)

answer = 0
I.reverse()
for i in range(1, N + 1):
    used[i] = False

for i in I:
    if used[i]:
        continue
    cnts = 0
    dfs2(i)
    answer += cnts * (cnts - 1) / 2

print(int(answer))