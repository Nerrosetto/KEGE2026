inp1 = int(input('Введите систему счисления (от 2 до 9): '))
inp2 = int(input('Введите число: '))
blank = ''
while inp2 != 0 and 2 <= inp1 <= 9:
    blank += str(inp2 % inp1)
    inp2 //= inp1
print(blank[::-1])