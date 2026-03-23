for x in range(37)[::-1]:
    num1 = 1 + 3 * 37 + x * 37 ** 2 + 8 * 37 ** 3 + 9 * 37 ** 4
    num2 = 4 + 2 * 37 + 9 * 37 ** 2 + x * 37 ** 3 + 1 * 37 ** 4
    num = num1 + num2
    if num % 21 == 0:
        print(x, num // 21)
        break
