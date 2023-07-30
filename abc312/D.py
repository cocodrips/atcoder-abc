MOD = 998244353
S = input()
N = len(S)
dp = [[0] * (N+1) for i in range(N+1)]

if N % 2 != 0:
    print(0)
    exit()

dp[0][0] = 1

for i in range(N):
    # i文字目
    c = S[i]
    for j in range(N):
        if c in ["(", "?"]:
            dp[i + 1][j + 1] += dp[i][j]
        if c in [")", "?"]:
            dp[i + 1][j - 1] += dp[i][j]
print(dp[N][0] % MOD)