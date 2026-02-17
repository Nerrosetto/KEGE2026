def F(n):
    if n < 3:
        return 1
    return F(n - 2) + 2 * n - 2 if n % 2 != 0 else F(n - 1) + n - 1


print(F(34))
