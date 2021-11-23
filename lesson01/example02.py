# Задание 2
# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

seconds = int(input("Введите количество секунд >>> "))

time_hour = seconds // 3600
seconds = seconds - (3600 * time_hour)
time_minute = seconds // 60
seconds = seconds - (60 * time_minute)
time_second = seconds

print("Время {}:{}:{}. В формате чч:мм:сс".format(time_hour, time_minute, time_second))
