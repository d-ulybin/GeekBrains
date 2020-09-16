"""5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
 Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
 Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
  Но если вместо числа вводится специальный символ, выполнение программы завершается.
   Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""
result = 0
while True:
    var_list = input('Вводите числа, разделенные пробелом, или введите "q" для выхода: ').split(',')
    try:
        for i, number in enumerate(var_list):
            quit_checker = number
            var_list[i] = int(number)
    except ValueError as e:
        if quit_checker.lower() == 'q' or quit_checker.lower() == ' q':
            for number in var_list:
                if type(number) == int:
                    result = result + number
            print(f'Сумма чисел равна {result}')
            break
        print('Введен(ы) не число(а)')
        continue
    result += sum(var_list)
    print(f'Сумма чисел равна {result}')
