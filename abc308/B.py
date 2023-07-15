
N, M = map(int, input().split(' '))
Colors = input().split(' ')
Dish = input().split(' ')
Price = list(map(int, input().split(' ')))

prices = {}
for d, p in zip(Dish, Price[1:]):
    prices[d] = p
sum = 0
for c in Colors:
    if c in prices:
        sum += prices[c]
    else:
        sum += Price[0]
print(sum)

