import collections
import heapq

# N = int(input())

N, S, T = list(map(int, input().split(' ')))
paths = [[] for i in range(N)]

for i in range(N - 1):
    u, v = list(map(int, input().split(' ')))
    paths[u - 1].append(v - 1)
    paths[v - 1].append(u - 1)

def dist_from(k: int):
    queue = []
    dist = [10 ** 9] * (N)
    dist[k] = 0
    shotest = [set() for _ in range(N)]
    # cost, place
    heapq.heappush(queue, (0, k, [k]))
    shotest[k].add(k)
    while len(queue) > 0:
        now_cost, now, path = heapq.heappop(queue)
        if now_cost > dist[now]:
            continue
        for to in paths[now]:
            if now_cost + 1 < dist[to]:
                dist[to] = now_cost + 1
                new_path = path[:]
                new_path.append(to)
                shotest[to] = set(new_path)
                heapq.heappush(queue, (now_cost + 1, to, new_path))
    return dist, shotest

dist_S, path_S = dist_from(S-1)
dist_T, path_T = dist_from(T-1)

for i in range(N):
    print(len(path_S[i] & path_T[i]))
