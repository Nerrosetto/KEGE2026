from string import ascii_uppercase, digits

with open(r'../Files/24_21421.txt') as file:
    data = file.readline()

alph = digits + ascii_uppercase

data1 = data
for i in alph[12:]:
    data1 = data1.replace(i, ' ')

data1 = data1.split()

ans = 0

for i in data1:
    ans = max(len(i.lstrip('0').rstrip('13579B')), ans)
print(ans)

print()
ans = 0
for i in alph[12:]:
    data = data.replace(i, ' ')

data = data.split()

for i in data:
    if i:
        while i and i[-1] in '13579B':
            i = i[:-1]
        while i and i[0] == '0':
            i = i[1:]
        ans = max(len(i), ans)
print(ans)
