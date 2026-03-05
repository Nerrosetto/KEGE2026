def f(start, end, cnt):
    if start > end or cnt >= 4:
        return 0
    if start == end:
        return 1
    return f(start + 2, end, cnt) + f(start + 3, end, cnt) + f(start * 2 + 1, end, cnt) if start % 2 == 0 else f(
        start + 2, end, cnt + 1) + f(start + 3, end, cnt + 1) + f(start * 2 + 1, end, cnt + 1)


print(f(1, 625, 0))
