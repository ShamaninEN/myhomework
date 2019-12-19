# first task
print('first task')

my_list = []
while True:
    input_string = input('Enter some string, if not press Enter: ')
    if len(input_string) > 0:
        new_string = input_string + '\n'
        my_list.append(new_string)
    else:
        last_el = my_list.pop()
        new_last_el = last_el[:-1]
        # print(new_last_el)
        # print(my_list)
        my_list.append(new_last_el)
        for i in my_list:
            f = open('file_for_first_task.txt', 'a', encoding='utf-8')
            f.write(i)
            f.close()
        break

try:
    my_file = open('file_for_first_task.txt', 'r', encoding='utf-8')
    content = my_file.readlines()
    print(content)
    my_file.close()
except:
    print('No such file or directory: "file_for_first_task.txt"')
finally:
    print('Next second task')

# second task
print('second task')
# The file takes from prewious task

try:
    my_f = open('file_for_first_task.txt', 'r', encoding='utf-8')
except:
    print('No such file or directory')

list_from_file = my_f.readlines()
print(list_from_file)
i = 0
while i < len(list_from_file):
    words_in_string = list_from_file[i].split()
    i = i + 1
    print(f'{i} strin contains {len(words_in_string)} words')

# third task
print('third task')

try:
    my_f = open('salary.txt', 'r', encoding='utf-8')
except:
    print('No such file or directory')

list_from_file = my_f.readlines()
average_salary = 0
workers = 0
for string in list_from_file:
    workers = workers + 1
    my_list = string.split()
    if int(my_list[1]) < 20000:
        print(f'{my_list[0]} salary {my_list[1]} {my_list[2]}')
        average_salary = average_salary + int(my_list[1])
    else:
        average_salary = average_salary + int(my_list[1])
print(f'Total salary {average_salary}, workers {workers}, average salary: {round(average_salary / workers)} rubles')

# fourth task
print('fourth task')


def write_file(str):
    my_num_f = open('numbers_rus.txt', 'a', encoding='utf-8')
    my_num_f.write(str)
    my_num_f.close()


numbers = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
f_num = open('numbers.txt', 'r')
str_num = f_num.readline()
while str_num:
    pars_str = str_num.split()
    str_num_rus = numbers[pars_str[0]] + ' ' + pars_str[1] + ' ' + pars_str[2] + '\n'
    write_file(str_num_rus)
    print(str_num_rus)
    str_num = f_num.readline()
f_num.close()
# fifth task
print('fifth task')

from random import randint
from functools import reduce

count = int(input('How many items need to the list: '))
min_list = int(input('Enter minimum item of list: '))
max_list = int(input('Enter maximum item of list: '))

nums_list = [str(randint(min_list, max_list)) + ' ' for i in range(count)]

with open('list_number.txt', 'w') as f:
    f.writelines(nums_list)

number_from_file = open('list_number.txt', 'r')
numb_from_file = number_from_file.read()
list_str_from_file = numb_from_file.split()
list_numb_from_file = []
for el in list_str_from_file:
    list_numb_from_file.append(int(el))
print(list_numb_from_file)


def reducer_func(el_prev, el):
    # el_prev — предшествующий элемент
    # el — текущий элемент
    return el_prev + el


print(f'Total: {reduce(reducer_func, list_numb_from_file)}')

# sixth task
print('sixth task')
lessons = {}
lesson_f = open('lessons.txt', 'r', encoding='utf-8')
les_str = lesson_f.readline()
while les_str:
    sobject, lecture, practice, lab = les_str.split()
    if lecture == '-':
        lecture = '0(л)'
    if practice == '-':
        practice = '0(пр)'
    if lab == '-':
        lab = '0(лаб)'
    lessons[sobject] = int(lecture[:-3]) + int(practice[:-4]) + int(lab[:-5])
    # print(lessons)
    les_str = lesson_f.readline()
print(lessons)

# seventh task
print('seventh task')
import json

report = {}
average_profit = 0
firms = 0
list_firm = []
firm_f = open('firm.txt', 'r', encoding='utf-8')
firm_str = firm_f.readline()
while firm_str:
    firm_name, org_struct, volume, expenses = firm_str.split()
    if int(volume) >= int(expenses):
        report[firm_name] = int(volume) - int(expenses)
        average_profit = average_profit + (int(volume) - int(expenses))
        firms = firms + 1
    else:
        report[firm_name] = int(volume) - int(expenses)

    firm_str = firm_f.readline()
list_firm.append(report)
list_firm.append({'average_profit': average_profit / firms})
print(list_firm)

with open('firm.json', 'w') as f_json:
    json.dump(list_firm, f_json)
