N = int(input())
# NM
scores = [[0 for i in range(100001)] for _ in range(2)]

sums = [0, 0]
for i in range(N):
    C, P = list(map(int, input().split(' ')))
    sums[C - 1] += P
    scores[0][i + 1] = sums[0]
    scores[1][i + 1] = sums[1]

Q = int(input())
for i in range(Q):
    L, R = list(map(int, input().split(' ')))
    print(scores[0][R] - scores[0][L-1], scores[1][R] - scores[1][L-1])