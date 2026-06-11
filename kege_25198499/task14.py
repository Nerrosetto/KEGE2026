from string import printable as pri

def perev(num,sys):
    a = ''
    while num:
        a += pri[num%sys]
        num //= sys
    return a[::-1]

maxi = 0
for x in range(1,2400):
    num = perev(7*9**210+6*9**110-x,9)
    if num.count('0') == 100:
       maxi = x
print(maxi)