def f(x, s):  # x - куча, s - сколько ходов осталось до конца игры.
    if x >= 40:
        return s % 2 == 0
    if s == 0:
        return False
    h = [f(x + 1, s - 1), f(x + 4, s - 1), f(x * 2, s - 1)]  # ходы
    return any(h) if (s - 1) % 2 == 0 else all(h)


print('19)', *[x for x in range(1, 40) if f(x, 2)])
print('20)', *[x for x in range(1, 40) if
               f(x, 3) and not f(x, 1)])  # Разрешает победить со второго хода, но не с первого хода.
print('21)', *[x for x in range(1, 40) if
               f(x, 4) and not f(x, 2)])
# print('21)', min([x for x in range(1, 40) if
#                f(x, 4) and not f(x, 2)])) # Если требуется найти минимальный ответ, можно добавить min.
