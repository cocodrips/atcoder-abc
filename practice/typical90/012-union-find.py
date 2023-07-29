from collections import defaultdict


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


H, W = list(map(int, input().split(' ')))
Query = int(input())

d = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
]


def mass(r, c):
    if 0 <= r < W and 0 <= c < H:
        return c * W + r
    return -1


ut = UnionFind(H * W)
red = [False] * (H * W)

for i in range(Query):
    in_ = list(map(int, input().split(' ')))
    if in_[0] == 1:
        r, c = in_[1:]
        base = mass(r - 1, c - 1)
        red[base] = True
        # print("same", ut.members(base))
        for dy, dx in d:
            index = mass(r - 1 + dy, c - 1 + dx)
            if index == -1:
                continue
            if red[index]:
                ut.union(base, index)

    if in_[0] == 2:
        Ra, Ca, Rb, Cb = in_[1:]
        ia = mass(Ra - 1, Ca - 1)
        ib = mass(Rb - 1, Cb - 1)
        if red[ia] and red[ib] and ut.same(ia, ib):
            print("Yes")
        else:
            print("No")
