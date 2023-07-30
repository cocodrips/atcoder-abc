from bisect import bisect_left, bisect_right
NSell, NBuy = list(map(int, input().split(' ')))

# 最低売値
Sell = sorted(list(map(int, input().split(' '))))
# 最高買値
Buy = sorted(list(map(int, input().split(' '))))

# りんごをn円でうってもいい人が、X円で買っても良い人以上

for value in sorted(Sell + list(map(lambda x: x +1, Buy))):
    sellable = bisect_right(Sell, value)
    # 予算value以上の人
    buyable = NBuy - bisect_left(Buy, value)

    # print(value, buyable, sellable)
    if buyable <= sellable:
        print(value)
        exit()
# 4 4
# 1 100 100 1000000000
# 100 100 100 100
