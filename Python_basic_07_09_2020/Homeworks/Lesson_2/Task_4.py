"""4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове."""

user_str = input('Введите строку из нескольких слов: ')
user_list = user_str.split()

for i, word in enumerate(user_list):
    print(i+1, word[:10])
