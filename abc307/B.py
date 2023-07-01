def main():
    N = int(input())
    v = []

    for i in range(N):
        v.append(input())

    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            p = v[i] + v[j]
            n = p[::-1]
            if p == n:
                print("Yes")
                return

    print("No")


main()


# 4
# a
# b
# a
# b