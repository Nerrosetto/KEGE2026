# Циклы

# # while - работает, ПОКА выполняется условие.

# # Операторы
# # continue - переходит к следующему шагу цикла.
# # break - останавливает работу цикла
# # else - выполняет блок кода если цикл завершился без break

# num = int(input())
# while num:
#     print(num % 10)
#     num //= 10

num = int(input())
num2 = []
while num >= 1:
    num2.append(num % 10)
    num //= 10
while num2:
    print(num2[-1])
    num2.remove(num2[-1])
