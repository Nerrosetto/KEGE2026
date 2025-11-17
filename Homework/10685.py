def convert(num, sys):
    res = ''
    while num != 0:
        res += str(num % sys)
        num //= sys
    return res[::-1]


re = []
for N in range(11, 200000):
    count0 = 0
    count1 = 0
    R = convert(N, 3)
    for i in R:
        if int(i) % 2 == 0:
            count0 += 1
        else:
            count1 += 1
    if count0 > count1:
        R = '22' + R
    else:
        R = '11' + R
    R = int(R, 3)
    if R > 100:
        re.append(R)
print(min(re))
