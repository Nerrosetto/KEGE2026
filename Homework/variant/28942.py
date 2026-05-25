def f(x, y):
    if x == y:
        return True
    if x < y or x == 73:
        return False
    return f(x - 3, y) + f(x - 8, y) + f(x // 2, y)


print(f(76, 41) * f(41, 12))
