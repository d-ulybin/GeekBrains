"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

try:
    with open("Text2.txt", "r", encoding="UTF-8") as file:
        counter = 0
        for i, line in enumerate(file):
            print(f"Строка №{i+1} - количество слов {len(line)}")
        print(f"Количество строк: {len(file.readlines())}")
except FileNotFoundError or FileExistsError:
    print("Ошибка, файл не существует или не найден.")
