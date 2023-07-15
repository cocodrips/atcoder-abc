class D:
    def __init__(self, a, b, _id):
        self.a = a
        self.b = b
        self._id = _id

    def __lt__(self, other):
        if self.a * other.b == self.b * other.a:
            return self._id < other._id
        return self.a * other.b > self.b * other.a

    def p(self):
        return str(self._id)

N = int(input())
succeed = []
for i in range(N):
    A, B = map(int, input().split(' '))
    succeed.append(D(A, B, i + 1))
succeed.sort()
print(' '.join([s.p() for s in succeed]))
