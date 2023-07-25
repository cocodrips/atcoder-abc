import collections
import sys
sys.setrecursionlimit(10 ** 5 + 10)

N = int(input())
connections = collections.defaultdict(list)
for i in range(N - 1):
    a, b = list(map(int, input().split(' ')))
    connections[a].append(b)
    connections[b].append(a)

visited = set()
res = []

def f(root):
    nexts = []
    for v in connections[root]:
        uv = tuple(sorted([root, v]))
        if uv in visited:
            continue
        nexts.append(v)
        visited.add(uv)
    if len(nexts) == 0:
        cur_sum = 1
    else:
        cur_sum = sum([f(i) for i in nexts]) + 1
    res.append(cur_sum * (N - cur_sum))
    return cur_sum

f(1)
print(sum(res))
