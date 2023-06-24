import itertools
import random

N = input()
v = sorted(map(int, input().split()))


# N = 60
# v = sorted([random.randrange(- 10 ** 2, 10 ** 2) for i in range(N)])

def get_min_max(vec):
    if len(vec) < 6:
        return vec
    return vec[:3] + vec[-3:]


posi = [i for i in v if i > 0]
nega = [i for i in v if i <= 0]

candidate = get_min_max(posi) + get_min_max(nega)
# print(candidate)

max_ = -10 ** 7
min_ = 10 ** 7

for a, b, c in itertools.combinations(candidate, 3):
    r = (a + b + c) / (a * b * c)
    max_ = max(max_, r)
    min_ = min(min_, r)

print(min_)
print(max_)

# 7
# -2 -4 4 5 5 5 5
