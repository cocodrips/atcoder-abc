import heapq
N = int(input())
A = list(map(int, input().split(' ')))

# 2つめのindexを答える
# 愚直: O(3N) memory, time

count = [0 for _ in range(N + 1)]
result = []
for i, a in enumerate(A):
    count[a] += 1
    if count[a] == 2:
        heapq.heappush(result, (i + 1, a))


print(" ".join([str(value) for _, value in result]))


