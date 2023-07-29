import collections

VertexLen = int(input())
Edges = collections.defaultdict(set)

for i in range(VertexLen - 1):
    a, b = list(map(int, input().split(' ')))
    Edges[a - 1].add(b - 1)
    Edges[b - 1].add(a - 1)


def dfs(vertex):
    distance = [-1] * VertexLen
    distance[vertex] = 0

    stack = [vertex]
    while stack:
        v = stack.pop()
        for next_v in Edges[v]:
            if distance[next_v] == -1:
                stack.append(next_v)
                distance[next_v] = distance[v] + 1

    return distance


v = dfs(0)
left = max([(v, i) for i, v in enumerate(v)])[1]
v = dfs(left)
print(max(v) + 1)