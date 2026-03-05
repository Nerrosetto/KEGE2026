def f(start, end, cnt):
    if start > end or '11' in cnt:
        return 0
    if start == end:
        return 1
    return f(start + 1, end, cnt + '1') + f(start + 2, end, cnt + '2') + f(start * 2, end, cnt + '3')


print(f(3, 11, '') * f(11, 24, '') + f(24, 79, ''))
