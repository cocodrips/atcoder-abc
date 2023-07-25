N, M = map(int, input().split(' '))
Ps, Cs, Fs = [], [], []

# 値段が安いほうが高い方のすべての機能をもつ
# 値段が低い製品は、高い製品にない機能を一つ以上もつ

for i in range(N):
    P, C, *F = map(int, input().split(' '))
    Ps.append(P)
    Cs.append(C)
    Fs.append(set(F))

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if Ps[i] <= Ps[j]:
            if Fs[j].issubset(Fs[i]) and (len(Fs[i] - Fs[j]) >= 1 or Ps[i] < Ps[j]):
                # print(j, i)
                print("Yes")
                exit()
print("No")

# 4 4
# 3 1 1
# 3 1 2
# 2 1 2
# 4 2 2 3
