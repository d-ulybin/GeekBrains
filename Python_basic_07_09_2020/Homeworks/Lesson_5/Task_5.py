"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

from random import randint

counter = randint(5, 20)

with open('text5.txt', 'w') as f_obj:
    for _ in range(counter):
        f_obj.write(f'{randint(1, 100)} ')

with open('text5.txt', 'r') as f_obj:
    content = f_obj.readline()

print(sum(map(int, content.split())))
