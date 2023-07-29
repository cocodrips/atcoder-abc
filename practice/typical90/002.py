N = int(input())

def f(i, current, text):
    if i == N and current == 0:
        print(text)
    if current < N - i:
        f(i+1, current+1, text + "(")
    if current > 0:
        f(i+1, current-1, text + ")")

f(0, 0, "")

