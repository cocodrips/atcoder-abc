def main(v):
    for i in range(8):
        if i > 0:
            if v[i] - v[i - 1] < 0:
                return False
        if v[i] < 100:
            return False
        if v[i] > 675:
            return False
        if v[i] % 25 != 0:
            return False
    return True



# N = int(input())
v = list(map(int, input().split(' ')))
if main(v):
    print('Yes')
else:
    print('No')