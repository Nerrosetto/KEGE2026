num = 0
N = int(input())
if N > 0 and N < 100:
    while N:
        if num == 2 or num == 3:
            print(num)
            N -= 1
        if num % 2 != 0 and num != 1 and num % 3 != 0:
            print(num)
            num += 1
            N -= 1
        else:
            num += 1
else:
    print('N > 100' if N >= 100 else 'N <= 0')