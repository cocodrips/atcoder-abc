N = int(input())
A = list(map(int, input().split(' ')))
S = list(input())
MEX = "MEX"
M = len(MEX)

def mex(a, b, c):
    for i in range(4):
        if a != i and b != i and c != i:
            return i

# [N][MEX(3)][1 << 3]
dp = [[[0 for mask in range(1 << M)] for j in range(M + 1)] for i in range(N + 1)]
print(dp)
