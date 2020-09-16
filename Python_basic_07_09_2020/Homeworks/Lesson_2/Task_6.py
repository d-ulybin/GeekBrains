"""* Реализовать структуру данных «Товары».
Она должна представлять собой список кортежей.
 Каждый кортеж хранит информацию об отдельном товаре.
 В кортеже должно быть два элемента — номер товара и словарь с параметрами
 (характеристиками товара: название, цена, количество, единица измерения). С
 труктуру нужно сформировать программно, т.е. запрашивать все данные у пользователя."""

name = 'Введите название товара: '
price = 'Введите цену товара: '
quantity = 'Введите количество товара: '
unit = 'Введите единицу измерения товара: '
item_list = []

while True:
    number = input('Определите количество товарных позиций: ')
    if number.isdigit():
        number = int(number)
        break
    print('Ошибка ввода!')

for index in range(0, number):
    user_name = input(name)
    while True:
        user_price = input(price)
        if user_price.isdigit():
            user_price = int(user_price)
            break
        print('Ошибка ввода!')
    while True:  # В этом моменте уже хочется написать функцию на проверку isdigit
        user_quantity = input(quantity)
        if user_quantity.isdigit():
            user_quantity = int(user_quantity)
            break
        print('Ошибка ввода!')
    user_unit = input(unit)
    temp_dict = {"название": user_name, "цена": user_price, "количество": user_quantity, "ед": user_unit}
    temp_set = ((index + 1), temp_dict)
    item_list.append(temp_set)

print(item_list)

item_analysis = {}
name_list = []
price_list = []
quantity_list = []
unit_list = []
temp_dict2 = {}

for i in range(0, number):
    temp_dict2 = item_list[i][1]
    name_list.append(temp_dict2.get('название'))
    price_list.append(temp_dict2.get('цена'))
    quantity_list.append(temp_dict2.get('количество'))
    unit_list.append(temp_dict2.get('ед'))

unit_list = list(set(unit_list))

item_analysis = {
    'название': name_list,
    'цена': price_list,
    'количество': quantity_list,
    'ед': unit_list
}
print(item_analysis)
