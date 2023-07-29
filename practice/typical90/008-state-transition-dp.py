# 最初のi文字目でjまで一致してるパターン数
MOD = 1000000007
N = int(input())
S = input()
atcoder = "atcoder"
dp = [
    [0 for j in range(len(atcoder) + 1)] for i in range(N + 1)
]
set()
dp[0][0] = 1
for i in range(N):
    for j in range(len(atcoder) + 1):
        dp[i+1][j] += dp[i][j]
        if j < len(atcoder) and S[i] == atcoder[j]:
            dp[i+1][j+1] += dp[i][j]

print(dp[N][len(atcoder)] % MOD)

