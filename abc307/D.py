
def main(v):
    answer = []
    left = 0
    for c in v:
        if c == '(':
            left += 1
            answer.append(c)
        elif c == ')':
            if left > 0:
                while True:
                    a = answer.pop()
                    if a == '(':
                        break
                left -= 1
            else:
                answer.append(c)
        else:
            answer.append(c)
    print(''.join(answer))

N = int(input())
v = list(input())
main(v)

#
# case = ['a(b(d))c', 'a(b)(', '()', ')))(((', 'a((bd))c']
# for c in case:
#     main(list(c))
