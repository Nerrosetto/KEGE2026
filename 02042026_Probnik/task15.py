def f(x, A):
    P = x in [i for i in range(15, 41)]
    Q = x in [i for i in range(21, 64)]
    return P <= (Q and (not (x in A)) <= (not P))

