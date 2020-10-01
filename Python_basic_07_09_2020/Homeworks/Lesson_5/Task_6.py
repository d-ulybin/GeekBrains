"""Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран."""

try:
    with open("Text6.txt", "r", encoding="UTF-8") as file:
        content = file.readlines()
except FileNotFoundError or FileExistsError:
    print("Ошибка, файл не существует или не найден.")

content = ['Информатика: 100(л) 50(пр) 20(лаб).\n', 'Физика: 30(л) — 10(лаб)\n', 'Физкультура: — 30(пр) —']
lessons_dict = {}
print(content)
sum_hours = 0
temp = ''
for line in content:
    for i, letter in enumerate(line):
        if letter.isdigit():
            temp = temp+letter
        elif line[i-1].isdigit() and not letter.isdigit():
            temp = float(temp)
            sum_hours += temp
            temp = ''
    line = line.split()
    lessons_dict[line[0]] = sum_hours
    sum_hours = 0

print(lessons_dict)
