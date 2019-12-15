# first task
print('first task')
def divide(x, y):
    z = x / y
    return z
while_1 = True
while while_1:
    try:
        a = float(input('Please enter first number: '))
    except:
        print('Please enter a number, try again')
        continue
    try:
        b = float(input('Please enter second number: '))
    except:
        print('Please enter a number, try again')
        continue
    try:
        print(divide(a, b))
    except:
        print('cannot be divided by 0, try again')
        continue
    else:
        while_1 = input("Repeat? if no press enter ")

# second task
print('second task')
def user_info(first_name,
              second_name,
              year_of_birth,
              city,
              email,
              number_phone):
    print(
        f'User: {first_name} {second_name}, born: {year_of_birth}, living: {city}, email: {email}, phone: {number_phone} ')


user_info(first_name='Vasia',
          second_name='Ivanov',
          year_of_birth='1976',
          city='Chelyabinsk',
          email='vasia@gmail.com',
          number_phone='89004322565')

# third task
print('third task')
def my_func(x, y, z):
    a = sum([x, y, z]) - min(x, y, z)
    return a


print(my_func(5, 5, 5))

# fourth task
print('fourth task')
def my_pow_func1(x, y):
    z = x ** y
    return z
print(my_pow_func1(2, -4))

def my_pow_func2(x, y):
    z = 1
    i = abs(y)
    while i != 0:
        z = z * x
        i = i - 1
    return 1/z
print(my_pow_func2(2, -4))

# fifth task
print('fifth task')
my_sum = 0


def sum_numbers(*args):
    sum_args = sum(args[0])
    return sum_args


my_while_stop = True
while my_while_stop:
    number_list = (input('Please enter numbers separated by spaces: ')).split()
    if len(number_list) > 0:
        real_number = []
        i = 0
        while i < len(number_list):
            if number_list[i].isdigit():
                real_number.append(int(number_list[i]))
                i = i + 1
            else:
                # print(f'Total: {my_sum + sum_numbers(real_number)}')
                my_while_stop = False
                break
        my_sum = my_sum + sum_numbers(real_number)
        print(f'Subtotal: {my_sum}')
    else:
        print('You entered nothing, try again')
print(f'Finish total: {my_sum}')

# sixth task
print('sixth task')
def int_func(str):
    my_new_str = str.capitalize()
    return my_new_str

input_str = (input('Enter words with a space: ')).split()
my_next_str = []

for word in input_str:
    my_next_str.append(int_func(word))
print(' '.join(my_next_str))



