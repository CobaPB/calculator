first_number = int(input('Введите число '))
second_number = int(input('Введите второе число '))
expression = input('Введите +,-,/,* ')
result = ''
if expression == '+':
    result = first_number + second_number
elif expression == '-':
    result = first_number - second_number
elif expression == '/':
    result = first_number / second_number
elif expression == '*':
    result = first_number * second_number
else:
    print('Поробуйте еще раз')
    exit()
print('Вывод ', result)
