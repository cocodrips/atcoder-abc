def PRINT(v):
    for i in range(len(v)):
        for j in range(len(v[0])):
            print(''.join(v[i][j]), end='')
        print()

def INPUT():
    H, W = list(map(int, input().split(' ')))
    AA = []
    for i in range(H):
        AA.append(list(input()))
    return H, W, AA
Ha, Wa, A = INPUT()
Hb, Wb, B = INPUT()
Hx, Wx, X = INPUT()

HH = 28
WW = 28

for hx1 in range(HH):
    for wx1 in range(WW):
        for hx2 in range(HH):
            for wx2 in range(WW):
                ans = [['.' for _ in range(HH)] for i in range(WW)]
                try:
                    for ha in range(Ha):
                        for wa in range(Wa):
                            if A[ha][wa] == '#':
                                ans[hx1 + ha][wx1 + wa] = '#'
                    for hb in range(Hb):
                        for wb in range(Wb):
                            if B[hb][wb] == '#':
                                ans[hx2 + hb][wx2 + wb] = '#'

                    for hc in range(Ha + Hb):
                        for wc in range(Wa + Wb):
                            answer = ans[hc:hc+Hx][wc:wc+Wx]
                            # PRINT(X)
                            # PRINT(answer)
                            # print("---")
                            if answer == X:
                                print('Yes')
                                exit()

                except:
                    break


print('No')

