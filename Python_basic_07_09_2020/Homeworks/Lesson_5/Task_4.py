"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

word_dict = {'One': 'Один',
             'Two': 'Два',
             'Three': 'Три',
             'Four': 'Четыре'}

try:
    with open("Text4.txt", "r", encoding="UTF-8") as file:
        while True:
            content = file.readline()
            if not content:
                break
            for key in word_dict.keys():
                if key in content:
                    content = content.replace(key, word_dict[key])
            with open('text4_new.txt', 'a', encoding='UTF-8') as f_obj:
                f_obj.write(content)
except FileNotFoundError or FileExistsError:
    print("Ошибка, файл не существует или не найден.")
