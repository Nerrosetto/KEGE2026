for i in range(100, 1000):
    num = ''
    num1 = int(str(i)[0]) + int(str(i)[1])
    num2 = int(str(i)[1]) + int(str(i)[2])
    for d in sorted([num1, num2])[::-1]:
        num += str(d)
    if num == '1412':
        print(i)
        break
