numX1 = int(input('X1: '), 18)
numY1 = int(input('Y1: '))
numX2 = int(input('X2: '), 18)
numY2 = int(input('Y2: '))
if not(abs(numX1) <= 19 and abs(numY1) <= 8 and abs(numX2) <= 19 and abs(numY2) <= 8):
    print('Неправильный значения.')
elif abs(numX1 - numX2) == 1 and abs(numY1 - numY2) == 2 or abs(numX1 - numX2) == 2 and abs(numY1 - numY2) == 1:
    print('Может.')
else:
    print('Не может.')