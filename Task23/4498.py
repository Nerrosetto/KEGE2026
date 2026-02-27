from functools import lru_cache


@lru_cache(None)
def f(start, end, way):
    if start > end:
        return 0
    if start == end and way.count('2') >= 2 and way.count('3') == 5:
        return 1
    return f(start * 5, end, way + '1') + f(start * 3, end, way + '2') + f(start + 45, end, way + '3') if way.count(
        '1') <= 4 else 0


print(f(1, 2970, ''))
