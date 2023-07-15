import heapq

N, K = list(map(int, input().split(' ')))
h = []
day_sum = 0
for i in range(N):
    A, B = list(map(int, input().split(' ')))
    day_sum += B
    heapq.heappush(h, (A, B))


ans = 1
while day_sum > K:
    day, n = heapq.heappop(h)
    day_sum -= n
    ans = day + 1
print(ans)