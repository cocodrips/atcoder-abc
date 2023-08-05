import collections
import heapq
N = int(input())
P = list(map(int, input().split(' ')))
if len(P) == 1:
    print(0)
else:
    print(max(0, max(P[1:]) + 1 - P[0]))