N, P, Q = map(int, input().split(' '))
D = map(int, input().split(' '))

min_ = P
for d in D:
    min_ = min(d + Q, min_)
print(min_)


