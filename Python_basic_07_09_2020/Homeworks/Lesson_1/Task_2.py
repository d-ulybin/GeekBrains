"""2. Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк."""

set_time = ''

while set_time.isdigit() is False:
    set_time = input('Please input correct time in sec:\n')

set_time = int(set_time)
hours = set_time // 3600
minutes = set_time % 3600 // 60
seconds = set_time % 3600 % 60

print(f"Your time is {hours} hours {minutes} minutes {seconds} seconds.")
