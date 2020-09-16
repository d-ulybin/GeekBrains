"""5. Запросите у пользователя значения выручки и издержек фирмы.
 Определите, с каким финансовым результатом работает фирма
 (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
  Выведите соответствующее сообщение. Если фирма отработала с прибылью,
  вычислите рентабельность выручки (соотношение прибыли к выручке).
  Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника."""

income = ''
expenses = ''

while income.isdigit() is False:
    income = input('Please input the income of the Company:\n')
while expenses.isdigit() is False:
    expenses = input('Please input the expenses of the Company:\n')

income = int(income)
expenses = int(expenses)

if expenses > income:
    print('Your company is unprofitable')
elif expenses == income:
    print('You work at zero')
else:
    print(f"Your P/L rate is {income / expenses}")
    employee_count = int(input('Please input the amount of employees in the Company:\n'))
    # Проверку на правильность ввода опускаем
    print(f"Your profit per employee is {income / employee_count}")
