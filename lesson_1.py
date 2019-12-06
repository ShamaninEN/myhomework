#первое задание

user_string =  input('введите что нибудь несколько знаков это будет строка: ')
print(user_string)
user_number_int =  int(input('введите целое число: '))
print(user_number_int)
user_number_float =  float(input('введите какое то число: '))
print(user_number_float)

#второе задание

value = int(input('введите количество секунд: '))
hours = value // 3600
minutes = (value % 3600) // 60
seconds = (value % 3600) % 60
print(f'Выводим в формате чч:мм:сс, {hours}:{minutes}:{seconds}')

#третье задание

value = int(input('введите число: '))
summa = value + value ** 2 + value ** 3
print(f'Найходим сумму чисел n + nn + nnn, {summa}')

#четвертое задание

value = input('введите целое положительное число: ')
big_value = 0
i = 0
while i < len(value):
    if big_value < int(value[i]):
        big_value = int(value[i])
    i = i + 1
print(big_value)

#пятое задание

proceeds = int(input('введите выручку: '))
costs = int(input('введите расходы: '))
# workers = input('Численность предприятия: ')
if proceeds > costs:
    # print('у вас прибыль')
    profit = proceeds - costs
    print(f'Ваша рентабильность выручки: {profit/proceeds}')
    workers = int(input('Численность работников: '))
    print(f'Прибыль на одного сотрудника: {profit / workers}')
else:
    print('У вас убыток')

#шестое задание

a = int(input('введите результат первого дня: '))
b = int(input('введите идеальный результат: '))
day = 1
while a <= b:
    a = a + a * 0.1
    day = day + 1
print(f'Спортсмену потребовалось дней: {day}')