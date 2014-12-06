
def solve(num, N):
    m = (N / 5) % 6
    num = num[m:] + num[:m]

    for j in xrange(N % 5):
        i = j % 5
        num = num[:i] + num[i + 1] + num[i] + (num[i + 2:] if i + 2 <= 5 else "")
    print num

if __name__ == "__main__":
    N = int(raw_input())
    num = "123456"
    solve(num, N)

