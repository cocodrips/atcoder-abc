# -*- coding: utf-8 -*-
# walkを使って解いてみる

n, m = map(int, raw_input().split())
friend = [[0 for _ in xrange(n)] for _ in xrange(n)]

for i in xrange(m):
    a, b = map(int, raw_input().split())
    a -= 1
    b -= 1
    friend[a][b] += 1
    friend[b][a] += 1

f = [[0 for _ in xrange(n)] for _ in xrange(n)]
for i in xrange(n):
    for j in xrange(n):
        d = 0
        for k in xrange(n):
            d += friend[i][k] * friend[k][j]
        f[i][j] = d

for i in xrange(n):
    s = 0
    for j in xrange(n):
        if i != j and friend[i][j] == 0 and f[i][j] > 0:
            s += 1
    print s

