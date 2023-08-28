prices = list(map(int, input().split(",")))

min_price = prices[0]
profit = 0
a = 0

for i in range(1, len(prices)):
    if prices[i] < prices[i - 1]:
        profit += prices[i - 1] - min_price
        min_price = prices[i]
        a += 1

    min_price = min(min_price, prices[i])

    if i == len(prices) - 1 and prices[i] >= prices[i - 1]:
        profit += prices[i] - min_price

print(profit)
