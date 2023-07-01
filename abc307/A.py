N = int(input())
v = list(map(int, input().split(' ')))
for i in range(N):
    start = i*7
    end = i*7+min(7, len(v))
    print(sum(v[start:end]), end=" ")
print()