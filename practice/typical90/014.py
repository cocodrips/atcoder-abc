N = int(input())
A = sorted(list(map(int, input().split(' '))))
B = sorted(list(map(int, input().split(' '))))
print(sum([abs(a - b) for a, b in zip(A, B)]))
