from functools import lru_cache


@lru_cache(None)
def f(start, end, flag24, flag32):
    if start == 24: flag24 = True
    if start == 32: flag32 = True
    if start == end and flag24 + flag32 == 1: return 1
    if start > end or flag24 + flag32 == 2: return 0
    return f(start + 1, end, flag24, flag32) + \
        f(start + 2, end, flag24, flag32) + \
        f(start + 4, end, flag24, flag32) + \
        f(start + 8, end, flag24, flag32)


print(f(16, 48, False, False))
