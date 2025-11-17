def convert(num, sys):
    res = ''
    while num != 0:
        res += str(num % sys)
        num //= sys
    return res[::-1]


re = []
for N in range(1, 200000):
    R = convert(N, 3)
    if N % 3 == 0:
        R += R[-2:]
    else:
        R += convert(sum(map(lambda x: int(x, 3), R)), 3)
    if int(R, 3) % 2 == 0 and int(R, 3) > 220:
        re.append(int(R, 3))
print(min(re))
