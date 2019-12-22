# second task
print('second task')

from random import randint
count = int(input('How many items need to the list: '))
min_list = int(input('Enter minimum item of list: '))
max_list = int(input('Enter maximum item of list: '))

nums_list = [randint(min_list, max_list) for i in range(count)]
my_new_nums_list = [el for i, el in enumerate(nums_list) if nums_list[i] > nums_list[i-1]]

print(nums_list)
print(my_new_nums_list)

# third task
print('third task')

print([el for el in range(20, 240) if el % 20 == 0 or el % 21 == 0])

# fourth task
print('fourth task')

mylist = [1, 2, 3, 1, 3, 4, 5, 6]
my_list_for_four_task = [el for el in mylist if mylist.count(el) == 1]
print(my_list_for_four_task)

# fifth task
print('fifth task')
from functools import reduce


def reducer_func(el_prev, el):
    # el_prev — предшествующий элемент
    # el — текущий элемент
    return el_prev * el


my_list_for_five_task = [el for el in range(100, 1001, 2)]
print(reduce(reducer_func, my_list_for_five_task))

# sixth task
print('sixth task')
# закоментировал потому как это бесконечные циклы и до следующих занятий не добраться.
# my_number = int(input('Enter number: '))
# from itertools import count, cycle
#
# for el in count(my_number):
#     print(el)
#
# a = [1,2,3,4,5,6]
#
# for el in cycle(a):
#     print(el)

# seventh task
print('seventh task')

from itertools import count
from math import factorial

def fibo_gen():
    for el in count():
        yield factorial(el)


x = 0
for i in fibo_gen():
    if x < 15:
        print(i)
        x += 1
    else:
        break