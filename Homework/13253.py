from itertools import product as per

END = []
DRA = []
cnt = 0
for i in set(per('КОНЕЦ', repeat=5)):
    i = ''.join(i)
    END.append(i)
for i in set(per('ДРАКОН', repeat=5)):
    i = ''.join(i)
    DRA.append(i)
print(len(set(END + DRA)))
