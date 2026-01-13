from itertools import permutations as per

alph = 'ХОЧУНАБЮДЖЕТ'
cnt = 0
for i in per(alph):
    i = ''.join(i).replace('О', '!').replace('У', '!').replace('А', '!').replace('Ю', '!').replace('Е', '!')
    if '!!!!!' not in i:
        cnt += 1
print(cnt)
