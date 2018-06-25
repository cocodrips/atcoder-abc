n = int(input())
ai = map(int, input().split())

count = 0
for a in ai:
    m = 1
    while (1 << m) <= a:
        if a % (1 << m) == 0:
            # print(a, 1 << m)
            count += 1
        else:
            break
        m += 1
print(count)