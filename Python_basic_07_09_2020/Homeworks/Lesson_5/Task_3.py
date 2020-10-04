"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
 Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
 Выполнить подсчет средней величины дохода сотрудников.
"""

try:
    with open("Text3.txt", "r", encoding="UTF-8") as file:
        content = file.readlines()
except FileNotFoundError or FileExistsError:
    print("Ошибка, файл не существует или не найден.")

salary = {}

# Формат строки:  "Иванов - 20000 рублей"
for line in content:
    temp = line.split()
    for item in temp:
        if item.isdigit():
            salary[temp[0]] = float(item)

value_sum = 0
for key, value in salary.items():
    value_sum += value
    if value < 20000:
        print(key)

print(f'Средняя зарплата сотрудников {value_sum / len(salary)}')

