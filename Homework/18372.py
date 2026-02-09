def f(num):
    d = []
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            d.append(i)
    if len(d) > 1 and str(int(sum(map(int, d)) / len(d)))[-2:] == '12':
        return str(int(sum(map(int, d)) / len(d)))
    else:
        return ''


cnt = 0
for i in range(770000)[::-1]:
    M = f(i)
    if M:
        cnt += 1
        print(i, M)
        if cnt == 5:
            break
