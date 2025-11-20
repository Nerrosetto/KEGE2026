def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]


for N in range(1, 9):
    b = 41
    c = 131
    a = ''
    d = ''
    while b != 0 or c != 0:
        if b != 0:
            a += convert(b, N)
        b //= N
        if c != 0:
            d += convert(c, N)
        c //= N
    if a[-1] == '2' and b[-1] == '1':
        print(N)
