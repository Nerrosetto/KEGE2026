from timeit import timeit


def vowels_censor(mess):
    result = ''
    for i in mess:
        if i in 'AEOIUaeoiu':
            continue
        else:
            result += i


def vowels_censor2(mess):
    result = ''
    for i in mess:
        if i not in 'AEOIUaeoiu':
            result += i


data = input()

time1 = timeit('vowels_censor(data)', globals=globals(), number=10000)
time2 = timeit('vowels_censor2(data)', globals=globals(), number=10000)
print(time1)
print(time2)
