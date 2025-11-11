for i in range(1, 20000):
    c = bin(i)[2::]
    d = ''
    if i % 5 == 0:
        c += c[-2] + c[-1] + c[-0]
    else:
        d = bin(i % 5 * 5)[2::]
        c += d
    if int(c, 2) > 256:
        print(i)
        break
