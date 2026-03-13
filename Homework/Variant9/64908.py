from functools import lru_cache


@lru_cache(None)
def f(start, end, way):
    if start > end or way.count('1') == 2:
        return 0
    if start == end:
        return 1
    return f(start - 1, end, way + '1') + f(start + 3, end, way + '2') + f(start * 2, end, way + '3') if way.count(
        '1') != 2 else 0


print(f(3, 12, ''))
