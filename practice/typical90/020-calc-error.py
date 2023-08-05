import math

a, b, c = list(map(int, input().split(' ')))
# if math.log(a, 2) < b * math.log(c, 2):
# print( a, c ** b)
if a < c ** b:
    print('Yes')
else:
    print('No')
