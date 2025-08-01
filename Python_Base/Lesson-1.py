num = 15
# id() - команда которая выдаёт номер ячейки памяти, где хранится переменная.
print(id(num))

# Целое число / integer / int
num = 20
print(type(num))

# Дробные числа / вещественные чилса / числа с плавающей точкой / float
fl_num = 3.14
print(type(fl_num))

# Строка / string / str
str1 = 'Str1'
str2 = "Str2"
print(type(str1))

# Список / list
lt = [9, 'hello', 7.99]
print(type(lt))

# Кортеж / tuple
tp = (56, 99, "poke", 0.6)
print(type(tp))

# Множество / set
st = {5, 7, 6, 5, 5, 5}
print(type(st))

# Словарь / dictionary / dict
client = {'name': 'Petrovich', 'weight': 90, 'born': 1930}
print(client['name'])
print(type(client))

# Логический тип / Булевый тип / boolean / bool
logic = True
print(type(logic))
