"""2. Для списка реализовать обмен значений соседних элементов,
т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input()."""

# Первый вариант решения
print('Вариант №1. Вводите данные в список. Если захотите завершить ввод, то введите "End"')
ask = ''
user_list = []
result_list = []

while True:
    ask = input('Введите элемент списка: ')
    if ask.lower() == 'end':
        break
    user_list.append(ask)

for i in range(1, len(user_list), 2):
    result_list.append(user_list[i])
    result_list.append(user_list[i - 1])

if len(user_list) % 2 != 0:
    result_list.append(user_list[-1])

print(f'Ваш список        {user_list}')
print(f'Измененный список {result_list}')

# Второй вариант решения (после методички)
print('Вариант №2. Вводите данные в список. Если захотите завершить ввод, то введите "End"')
ask2 = ''
user_list2 = []
result_list2 = []
counter = 0
temp_list = []

while True:
    ask2 = input('Введите элемент списка: ')
    if ask2.lower() == 'end':
        break
    counter += 1
    user_list2.append(ask2)
    if counter % 2 == 0:
        temp_list = user_list2[counter - 2:counter]
        temp_list.reverse()
        result_list2.extend(temp_list)

if len(user_list2) % 2 != 0:
    result_list2.append(user_list2[-1])

print(f'Ваш список        {user_list2}')
print(f'Измененный список {result_list2}')
