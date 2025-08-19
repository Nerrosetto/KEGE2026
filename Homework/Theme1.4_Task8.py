num = int(input('Введите свой возраст.'))
if num < 7:
    print('Дошкольный')
elif num <= 7 and num < 18:
    print('Школьник.')
elif num <= 18 and num < 22:
    print('Студент.')
elif num <= 22 and num < 65:
    print('Рабочий.')
else:
    print('Пенсионер.')
