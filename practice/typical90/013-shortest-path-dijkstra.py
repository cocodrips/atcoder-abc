import collections
import heapq

N, M = list(map(int, input().split(' ')))

paths = [[] for i in range(N+1)]
for i in range(M):
    A, B, C  =list(map(int, input().split(' ')))
    paths[A].append((B, C))
    paths[B].append((A, C))


def dist_from(k: int):
    queue = []
    dist = [10 ** 9] * (N+1)
    dist[k] = 0
    # cost, place
    heapq.heappush(queue, (0, k))
    while len(queue) > 0:
        now_cost, now = heapq.heappop(queue)
        if now_cost > dist[now]:
            continue
        for to, cost in paths[now]:
            if now_cost + cost < dist[to]:
                dist[to] = now_cost + cost
                heapq.heappush(queue, (now_cost + cost, to))
    return dist

dist_1 = dist_from(1)
dist_n = dist_from(N)

for i in range(N):
    print(dist_1[i+1] + dist_n[i+1])