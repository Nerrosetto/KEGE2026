from itertools import product as per

END = []
DRA = []
ee = []
cnt = 0
for i in set(per('КОНЕЦ', repeat=5)):
    i = ''.join(i)
    END.append(i)
for i in set(per('ДРАКОН', repeat=5)):
    i = ''.join(i)
    DRA.append(i)
for i in set(per('КОН', repeat=5)):
    i = ''.join(i)
    ee.append(i)
print(len(END) + len(DRA) - 2 * len(ee))
