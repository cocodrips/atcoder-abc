import heapq

N, K = list(map(int, input().split(' ')))

scores = []
best = []
heapq.heapify(best)

def add(v):
    if len(best) < K:
        heapq.heappush(best, v)
    else:
        head = best[0]
        if head < v:
            heapq.heappop(best)
            heapq.heappush(best, v)

for i in range(N):
    full, part = list(map(int, input().split(' ')))
    add(part)
    add(full - part)

print(sum(best))
