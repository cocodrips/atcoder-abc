# -*- coding: utf-8 -*-
# 行列の2乗

n = 10
array = [[0 for _ in xrange(n)]  for _ in xrange(n)]
result = [[0 for _ in xrange(n)]  for _ in xrange(n)]
for i in xrange(n):
    for j in xrange(n):
        d = 0
        for k in xrange(n):
            d += array[i][k] * array[k][j]
        result[i][j] = d