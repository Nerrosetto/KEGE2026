from string import printable as pri
from itertools import product as pro


def convert(x, sys):
    a = ''
    while x:
        a += pri[x % sys]
        x //= sys
    return a[::-1]


for p in range(int(max('boomblcng'), 36) + 1, 37):
    if int('bo', p) + int('om', p) + int('bl4', p) == int('cng', p):
        print(int(p))
