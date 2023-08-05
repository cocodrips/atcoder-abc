N = int(input())
A, B, C = list(map(int, input().split(' ')))

MIN = 10000
for a in range(10000):
    for b in range(10000 - a):
        n = N
        n -= A * a
        n -= B * b
        if n >= 0 and n % C == 0:
            c = n // C
            MIN = min(MIN, a + b + c)
print(MIN)




