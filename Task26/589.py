from math import floor

with open(r'./Files/26_589.txt') as file:
    N = int(file.readline())
    prices = [int(i) for i in file]

prices = sorted(prices)
prices_on_sale = []
summi = 0
max_sale = 0
for i in range(0, max(prices), 500):
    prices_on_sale = [t for t in prices if i < t < i + 500]
    summi += sum(prices_on_sale[:len(prices_on_sale) // 2]) / 2
    max_sale = max(max_sale, max(prices_on_sale[:len(prices_on_sale) // 2]))

print(summi, floor(max_sale / 2))
