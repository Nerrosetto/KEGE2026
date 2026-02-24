def f(start, end):
    if start == end:
        return 1
    if start > end:
        return 0
    return f(start + 2, end) + f(start + 5, end) + f(start ** 2, end)


print(f(4, 36) - 1)

########################################
print('_' * 10)


def fa(start, end, last):
    if start == end and last != 'C':
        return 1
    if start > end:
        return 0
    return fa(start + 2, end, 'A') + fa(start + 5, end, 'B') + fa(start ** 2, end, 'C')


print(fa(4, 36, ''))
