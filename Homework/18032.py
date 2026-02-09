def f(num):
    d = []
    for i in range(1, num + 1):
        if num % i == 0:
            d.append(i)
    return str(sum(map(int, d)))


cnt = 0
for num in range(1000, 10000):
    if str(f(num))[-2:] == '23':
        cnt += 1
        print(num, f(num))
        if cnt == 5:
            break
