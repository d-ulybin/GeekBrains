"""4. Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции."""

number = ''

while number.isdigit() is False:
    number = input('Please input a number:\n')

number = int(number)
big_number = 0

while number:
    temp = number % 10
    number = number // 10
    if temp > big_number:
        big_number = temp

print(big_number)
