import collections

N = int(raw_input())
time = collections.defaultdict(int)
for i in xrange(N):
    s, e = map(int, raw_input().split('-'))
    s = s - s % 5
    if e % 5 != 0:
        e = e + (5 - e % 5)
    time[s] += 1
    time[e] -= 1

n = 0
start = []
end = []
for s, m in sorted(time.items()):
    if m == 0:
        continue
    if n == 0:
        start.append(s)
    n += m
    if n == 0:
        end.append(s)

for s, e in zip(start, end):
    print "{0:0<4}".format(s) + "-" + "{0:0<4}".format(e)

