N, L = list(map(int, input().split(' ')))
K = int(input())
A = list(map(int, input().split(' ')))
A = [0] + A + [L]
left, right = 0, L

def enable(minimum):
    length = 0
    cuts = []
    for c1, c2 in zip(A, A[1:]):
        length += c2 - c1
        if length >= minimum:
            cuts.append(length)
            length = 0
    else:
        # さいごのひとかけら
        if length >= minimum:
            cuts.append(length)
    return len(cuts) >= K + 1


while right - left > 1:
    mid = (left + right) // 2
    # print(left, right, "mid: ", mid)
    if enable(mid):
        left = mid
    else:
        right = mid
print(left)
