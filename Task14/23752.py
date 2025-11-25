from string import printable as al


def convert(num, sys):
    res = ''
    while num:
        res += al[num % sys]
        num //= sys
    return res[::-1]


num = 2 * 2187 ** 2020 + 729 ** 2021 - 2 * 243 ** 2022 + 81 ** 2023 - 2 * 27 ** 2024 - 6561
num_27 = convert(num, 27)
cou = 0
res = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in num_27:
    if int(i, 27) > 9:
        cou += 1
print(cou)
cou = 0
print('____________________________' * 8)
for i in num_27:
    if res.count(int(i, 27)) == 0:
        cou += 1
print(cou)
cou = 0
print('____________________________' * 8)
for i in al[10:27]:
    cou += num_27.count(i)
print(cou)
cou = 0
print('____________________________' * 8)
for i in num_27:
    if i in al[10:27]:
        cou += 1
print(cou)
