def convert(num, sys):
    ans = ''
    while num:
        ans += str(num % sys)
        num //= sys
    return ans[::-1]


res = []
num = convert(15625 ** 16 - 3125 ** 3 * 25 ** 19 + 625 ** 4 - 2005, 5)
print(num.count('0'))
print('_' * 100)
num = 15625 ** 16 - 3125 ** 3 * 25 ** 19 + 625 ** 4 - 2005
cnt = 0
while num:
    if num % 5 == 0:
        cnt += 1
    num //= 5
print(cnt)
