from fnmatch import fnmatch as fnm
from itertools import product as pro


def not_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return True
    return False


ans = []
for l1 in range(1, 5):
    for N in range(10 ** (l1 - 1), 10 ** l1):
        if not_prime(N):
            for l2 in range(0, 4 - l1 + 1):  # Возможная длина числа на месте первой звезды
                for z1 in pro('0123456789', repeat=l2):  # Первая звезда в числе.
                    z1 = ''.join(z1)
                    for l3 in range(0, 4 - l1 - l2 + 1):  # Возможная длина числа на месте второй звезды
                        for z2 in pro('0123456789', repeat=l3):  # Вторая звезда в числе.
                            z2 = ''.join(z2)
                            num = int(f'1{N}03{z1}6{z2}')
                            if num % 22768 == 0 and num < 10 ** 8:
                                ans.append([num, N])
for i in sorted(ans):
    print(*i)
#####################
ans = []
for N in range(4, 10000):
    if not_prime(N):
        ans.append(N)

ansii = []
for N in ans:
    num_mask = int(f'1{N}036')
    for num in range(num_mask - num_mask % 22768, 10 ** 8, 22768):
        if fnm(str(num), f'1{N}03*6*'):
            ansii.append([num, N])

for i in sorted(ansii):
    print(*i)
