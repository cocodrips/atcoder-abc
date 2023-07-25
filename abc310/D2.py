# Reference: https://atcoder.jp/contests/abc310/submissions/43534034
N, T, M = map(int, input().split())
A, B = [], []
for _ in range(M):
    a, b = map(int, input().split())
    A.append(a - 1)
    B.append(b - 1)

def f(n, team, num_team):
    if n == N:
        # 決まったチームの数ならOK
        if num_team != T:
            return 0
        ret = 1
        # ngが全部満たされれば1
        for i in range(M):
            ret &= team[A[i]] != team[B[i]]
    else:
        ret = 0
        for i in range(num_team + 1):
            team[n] = i
            ret += f(n + 1, team, max(num_team, i + 1))
    return ret

print(f(0, [-1] * N, 0))