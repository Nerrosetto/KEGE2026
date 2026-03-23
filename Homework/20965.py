def f(start, mov):
    if start <= 13:
        return mov % 2 == 0
    if mov == 0:
        return False
    h = [
        f(start - 3, mov - 1),
        f(start // 1.5, mov - 1),
    ]
    return any(h) if (mov - 1) % 2 == 0 else all(h)


print('19)', min(*[x for x in range(14, 40) if f(x, 2)]))
print('20)', [*[x for x in range(14, 40) if
               f(x, 3) and not f(x, 1)]][:2])
print('21)', min(*[x for x in range(14, 40) if
               f(x, 4) and not f(x, 2)]))
