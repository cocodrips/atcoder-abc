def print_matrix(array):
    for a in array:
        print a


if __name__ == "__main__":
    n, m = map(int, raw_input().split())

    friend = [[] for _ in xrange(n)]
    for i in xrange(m):
        a, b = map(int, raw_input().split())
        a -= 1
        b -= 1
        friend[a].append(b)
        friend[b].append(a)

    for i, f in enumerate(friend):
        c = 0
        used = []
        for ff_i in f:
            for fff in friend[ff_i]:
                if fff != i and fff not in f and fff not in used:
                    used.append(fff)
                    c += 1
        print c
