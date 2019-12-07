# первое задание

my_list = [1, 2, 5, 23.34, 'fadagas', [34, '6446', False], {'one': 'string', 1: [2, 5, 'string']}, (1, 5, 'fsa'), {1, 4, 6}]
a = [1, 2, 3, 23.34]
i = 0
while i < len(my_list):
    print(type(my_list[i]))
    i = i + 1

# второе задание
a = input('Введите данные списка через пробел: ')
my_list_2 = a.split(' ')
my_next_list = []
my_list_2_new = []
i = 0
b = False
if len(my_list_2) == 1:
    print('Вы ничего не ввели или ввели только одно значение поэтому и не увидете мой шедевральный код с кучами ифов')
elif len(my_list_2) % 2 != 0:
    b = my_list_2.pop()
    my_next_list = my_list_2
else:
    my_next_list = my_list_2
while i < len(my_next_list):
    my_list_2_new.append(my_list_2[i + 1])
    my_list_2_new.append(my_list_2[i])
    i = i + 2
if b:
    my_list_2_new.append(b)
if len(my_list_2_new) > 0:
    print(my_list_2_new)

# третье задание

months_list = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
month_dict = {1: 'январь',
              2: 'февраль',
              3: 'март',
              4: 'апрель',
              5: 'май',
              6: 'июнь',
              7: 'июль',
              8: 'август',
              9: 'сентябрь',
              10: 'октябрь',
              11: 'ноябрь',
              12: 'декабрь'}
try:
    value = int(input('Введите номер месяца: '))
except:
    print('Пожалуйста введите номер месяца цифрой')
    value = int(input('Введите номер месяца: '))

while value <= 0 or value > 12:
    print('Нет такого месяца')
    value = int(input('Введите номер месяца: '))
if 0 < value < 13:
    # use list
    print(f'месяц: {months_list[value - 1]}')
    # use dict
    print(f'месяц: {month_dict[value]}')

# четвертое задание

user_value = input('введите строку из нескольких слов, разделённых пробелами: ')
user_value_list = user_value.split(' ')
for word in user_value_list:
    print(word[:10])

# пятое задание

my_list_5 = [7, 5, 3, 3, 2]
my_list_5.reverse()
try:
    c = int(input('введите рейтинг: '))
except:
    print('Введите целое число')
    c = int(input('введите рейтинг: '))
if c < my_list_5[0]:
    my_list_5.insert(0, c)
elif c > my_list_5[len(my_list_5) - 1]:
    my_list_5.insert(len(my_list_5), c)
else:
    count_c = my_list_5.count(c)
    if count_c > 0:
        search = my_list_5.index(c)
        my_list_5.insert(search, c)
    else:
        i = 0
        while i < len(my_list_5):
            if my_list_5[i] < c < my_list_5[i+1]:
                my_list_5.insert(i+1, c)
                break
            else:
                i = i + 1
my_list_5.reverse()
print(my_list_5)
