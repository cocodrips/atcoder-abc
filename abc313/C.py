import math
import collections
import heapq

N = int(input())
A = list(map(int, input().split(' ')))

mid = sum(A) / len(A)
low = int(math.floor(mid))
high = int(math.ceil(mid))

plus = 0
minus = 0
count = 0

for a in A:
    if a < mid:
        plus += abs(low - a)
    else:
        minus += abs(a - high)

print(max(plus, minus))
