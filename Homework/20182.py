def convert(num, sys):
    res = ''
    while num != 0:
        res += str(num % sys)
        num //= sys
    return res[::-1]


re = []
for N in range(1, 200000):
    R = convert(N, 3)
    if sum(map(lambda x: int(x, 3), R)) % 2 == 0:
        R = '12' + R[2:] + '0'
    else:
        R = '10' + R[2:] + '2'
    R = int(R, 3)
    if R > 105:
        re.append(N)
print(min(re))
