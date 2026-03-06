def convert_10(num, sys):
    num = num[::-1]
    number = 0
    for i in range(len(num)):
        number += int(num[i], 36) * sys ** i
    return number


for p in range(33, 100):
    num = convert_10('kot', p) + convert_10('golodni', p)
    if num == convert_10('meeow', p) * convert_10('100', p) - 20194023088:
        print(convert_10('purr', p))
        break
