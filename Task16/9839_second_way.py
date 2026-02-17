from sys import setrecursionlimit


def F(n):
    return 2 * n + 5 + F(n - 2) if n >= 3 else 3


setrecursionlimit(1600)
print(F(3027) - F(3023))
