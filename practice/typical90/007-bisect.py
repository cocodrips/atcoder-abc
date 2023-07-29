from bisect import bisect_left

N = int(input())
A = sorted(list(map(int, input().split(' '))))
Q = int(input())

for i in range(Q):
    B = int(input())
    idx = bisect_left(A, B)
    print(min(abs(A[idx % N] - B), abs(A[idx - 1] - B)))
