# Задание 3
# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

n = input("Введите ваше число n >>> ")

sum = int(n) + int(n * 2) + int(n * 3)
print("n + nn + nnn = ", sum)
