# Задание 4
# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input("Введите целое положительное число >>> "))
max_number = -1

while number > 1:
    one_time_number = number % 10
    number //= 10
    if one_time_number > max_number:
        max_number = one_time_number

print(max_number)
