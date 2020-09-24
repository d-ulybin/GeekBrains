"""
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
"""

from itertools import cycle, count
from time import sleep

for el in count(3):
    if el > 10:
        break
    else:
        print(el)

counter = 0
for el in cycle([300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]):
    if counter > 20:
        break
    print(el, end='; ')
    sleep(0.5)
    counter += 1
