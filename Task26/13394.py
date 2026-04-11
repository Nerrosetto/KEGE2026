from math import floor

with open(r'./Files/26.6_13394.txt') as file:
    N = int(file.readline())
    item_prices = [int(i) for i in file]


k = 3
all_item_prices = sorted(item_prices, reverse=True)
on_sale = [i for i in all_item_prices if i > 350]
many = sum(all_item_prices) - sum(floor(i * 0.75) for i in on_sale[k - 1::k])
single = sum(all_item_prices) - floor(sum(on_sale[-len(on_sale) // k:]) * 0.75)
print(f'{many} , {single}')
