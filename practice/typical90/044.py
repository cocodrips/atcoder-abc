N, Q = list(map(int, input().split(' ')))
A = list(map(int, input().split(' ')))

start = 0

for i in range(Q):
    t, x, y = list(map(int, input().split(' ')))
    x -= 1
    y -= 1
    if t == 1:
        # swap
        tmp = A[(x + start) % N]
        A[(x + start) % N] = A[(y + start) % N]
        A[(y + start) % N] = tmp
    if t == 2:
        start -= 1
    if t == 3:
        print(A[(x + start) % N])
    # print(A)


