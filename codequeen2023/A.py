import collections
import heapq
S = input()
x = input()
s = ""
for c in S:
    if c != x:
        s += c
    else:
        s += c + c
print(s)

