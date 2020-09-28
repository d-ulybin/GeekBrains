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

for key, value in salary.items():
    if value < 20000:
        print(key)


