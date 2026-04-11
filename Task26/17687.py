with open(r'./Files/26_17687.txt') as file:
    N = int(file.readline())
    items_prices = [int(i) for i in file]

prices = sorted(items_prices, reverse=True)
K = len(prices)
price_customer = sum(prices) - sum(prices[:K // 9])
price_shop = sum(prices) - sum(prices[K - 1::9])
print(f'{price_customer} , {price_shop}')
