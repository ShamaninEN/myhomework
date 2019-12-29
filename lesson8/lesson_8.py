# first task
print('first task')


class Date(object):
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_str):
        day, month, year = map(int, date_as_str.split('-'))
        my_date = cls(day, month, year)
        return my_date

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999



print(Date.is_date_valid('15-09-2012'))
print(Date.is_date_valid('15-39-2012'))
new_date = Date.from_string('11-09-2012')

print(new_date.day)

# second task
print(' ')
print('second task')

class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

dividend = input("Введите делимое число: ")
divider = input("Введите делительо: ")
try:
    if dividend.isdigit() != True:
        raise OwnError("Вместо делителя вы ввели хз чего")
except OwnError as err:
    print(err)
finally:
    print('Едем дальше')

try:
    if int(divider) == 0:
        raise OwnError("На ноль делить нельзя")
except ValueError:
    print("Вы ввели не число")
except OwnError as err:
    print(err)
else:
    try:
        value = int(dividend) / int(divider)
    except ValueError:
        print("Т.к. вы ввели не число у вас ничего не получиться")
    else:
        print(f"Все хорошо. Результат: {value}")
finally:
    print('Конец задачи')

# third task
print(' ')
print('third task')

class My_Error(Exception):
    def __init__(self, txt):
        self.txt = txt

    def __str__(self):
        return self.txt

    @staticmethod
    def check_numb(numb):
        return numb.isdigit()

    @classmethod
    def my_list(cls):
        stop = True
        my_list = []
        while stop:
            entr_numb = input('Enter a number or press "q": ')
            if My_Error.check_numb(entr_numb):
                my_list.append(entr_numb)
            else:
                if entr_numb == 'q':
                    stop = False
                    print(my_list)
                else:
                    my_err = cls("You entered not a number ")
                    print(my_err)


My_Error.my_list()

# fourth task
print(' ')
print('fourth task')

class My_Numb_Valid(Exception):
    def __init__(self, txt):
        self.txt = txt

    def __str__(self):
        return self.txt

    @staticmethod
    def check_numb(numb):
        return numb.isdigit()


class Storage:
    """ Класс storage сщдержит наименование и списки словарей
    содержащихся товаров на складе и
    2 метода один на приемку товара а второйй на перемещение.
    По логике данной программы склад централизованный и
    в первую очередь заполняется товаром главный склад,
    а после того как он заполнен можно приступать к перемещению товара на другой склад.
    Складской учет ведется поштучно. Т.е. каждая единица техники заносится отдельно
    и перемещать можно только то что есть на складе. """
    def __init__(self, name):
        self.name = name
        self.printer_quantity = []
        self.scanner_quantity = []
        self.copier_quantity = []

    @property
    def to_storage(self):
        """ Вам будет предложено выбрать 3 действия
        заполнить склад, посмотреть отчет по складу и перейти к перемещению. При выборе первого варианта
        вам так же будет предложено выбрать что поступает на склад, принтер ксерокс или факс. """
        run = True
        while run:
            action = input(' 1 - income on storage \n '
                           '2 - storage report \n '
                           'q - quit \n '
                           'Please select an actions: ')
            if action == '1':
                add_somthing = True
                while add_somthing:
                    select_technic = input(' 1 - printer \n'
                                           '2 - scanner \n'
                                           '3 - copier \n'
                                           ' q - quit \n '
                                           'Please select a technic: ')
                    if select_technic == '1':
                        printer = Printer(input('Enter printer name: '),
                                          int(input('Enter printer resolution: ')),
                                          int(input('Enter printer speed: ')),
                                          int(input('Enter printer price: ')))
                        print(f'You add {printer.name} price {printer.price}')
                        self.printer_quantity.append({'printer': printer.name,
                                                      'resolution': printer.resolution,
                                                      'speed': printer.speed,
                                                      'price': printer.price})
                    elif select_technic == '2':
                        scanner = Scanner(input('Enter scanner name: '),
                                          int(input('Enter scanner resolution: ')),
                                          int(input('Enter scanner speed: ')),
                                          int(input('Enter scanner price: ')))
                        print(f'You add {scanner.name} price {scanner.price}')
                        self.scanner_quantity.append({'scanner': scanner.name,
                                                      'resolution': scanner.resolution,
                                                      'speed': scanner.speed,
                                                      'price': scanner.price})
                    elif select_technic == '3':
                        copier = Copier(input('Enter copier name: '),
                                        int(input('Enter copier resolution: ')),
                                        int(input('Enter copier speed: ')),
                                        int(input('Enter copier price: ')))
                        print(f'You add {copier.name} price {copier.price}')
                        self.copier_quantity.append({'copier': copier.name,
                                                     'resolution': copier.resolution,
                                                     'speed': copier.speed,
                                                     'price': copier.price})
                    elif select_technic == 'q':
                        # print(select_technic)
                        add_somthing = False
                    else:
                        print('somthing wrong')
            elif action == '2':
                print(self.printer_quantity)
                print(self.scanner_quantity)
                print(self.copier_quantity)
            elif action == 'q':
                # print(action)
                run = False
            else:
                print('somthing wrong')
        pass

    @property
    def from_storage(self):
        """ Как уже было сказано перемещать можно только то что есть на складе.
        Вам будет необходимо выбрать что хотите переместить: принтер ксерокс или сканер, а затем
        будет показан список данной позицыи на складе и вам нужно ввести порядковы2 номер изделия.
        Выбранный товар переместиться с основного склада на вторичный.
        По условиям задачи добавил собственный валидатор, который сообщает о том если введен номер товара,
        больший чем есть товара на складе, но что бы не прерывать процесс, перемещается самый последний товар."""
        run = True
        while run:
            action = input(' 1 - moving between storage \n '
                           '2 - storage report \n '
                           'q - quit \n '
                           'Please select an actions: ')
            if action == '1':
                add_somthing = True
                while add_somthing:
                    select_technic = input(' 1 - printer \n'
                                           '2 - scanner \n'
                                           '3 - copier \n'
                                           ' q - quit \n '
                                           'Please select a technic: ')
                    if select_technic == '1':
                        print(f'List of printers for moving {self.printer_quantity}')
                        print(f'Numbers of printer for moving {len(self.printer_quantity)}')
                        number_printer = int(input('Enter number of printer for moving: ')) - 1
                        try:
                            if number_printer > len(self.printer_quantity):
                                number_printer = len(self.printer_quantity) - 1
                                raise My_Numb_Valid('Dont have this technic')
                        except My_Numb_Valid as err:
                            print(err)

                        print(f'You chose {self.printer_quantity[number_printer]["printer"]} price {self.printer_quantity[number_printer]["price"]}')
                        moving_item = self.printer_quantity.pop(number_printer)
                        print(moving_item)
                        second_storage.printer_quantity.append(moving_item)
                        print(f'Report {self.name} after moving {self.printer_quantity}')
                        print(f'Report {second_storage.name} after moving {second_storage.printer_quantity}')
                    elif select_technic == '2':
                        print(f'List of scanner for moving {self.scanner_quantity}')
                        print(f'Numbers of scanner for moving {len(self.scanner_quantity)}')
                        number_scanner = int(input('Enter number of scanner for moving: ')) - 1
                        try:
                            if number_scanner > len(self.scanner_quantity):
                                number_scanner = len(self.scanner_quantity) - 1
                                raise My_Numb_Valid('Dont have this technic')
                        except My_Numb_Valid as err:
                            print(err)
                        print(f'You chose {self.scanner_quantity[number_scanner]["scanner"]} price {self.scanner_quantity[number_scanner]["price"]}')
                        moving_item = self.scanner_quantity.pop(number_scanner)
                        print(moving_item)
                        second_storage.scanner_quantity.append(moving_item)
                        print(f'Report {self.name} after moving {self.scanner_quantity}')
                        print(f'Report {second_storage.name} after moving {second_storage.scanner_quantity}')
                    elif select_technic == '3':
                        print(f'List of copier for moving {self.copier_quantity}')
                        print(f'Numbers of copier for moving {len(self.copier_quantity)}')
                        number_copier = int(input('Enter number of printer for moving: ')) - 1
                        try:
                            if number_copier > len(self.copier_quantity):
                                number_copier = len(self.copier_quantity) - 1
                                raise My_Numb_Valid('Dont have this technic')
                        except My_Numb_Valid as err:
                            print(err)
                        print(f'You chose {self.copier_quantity[number_copier]["copier"]} price {self.copier_quantity[number_copier]["price"]}')
                        moving_item = self.copier_quantity.pop(number_copier)
                        print(moving_item)
                        second_storage.copier_quantity.append(moving_item)
                        print(f'Report {self.name} after moving {self.copier_quantity}')
                        print(f'Report {second_storage.name} after moving {second_storage.copier_quantity}')
                    elif select_technic == 'q':
                        # print(action)
                        add_somthing = False
                    else:
                        print('somthing wrong')
            elif action == '2':
                print(f'Storage {self.name} include {self.printer_quantity}')
                print(f'Storage {second_storage.name} include {second_storage.printer_quantity}')
                print(f'Storage {self.name} has {self.scanner_quantity}')
                print(f'Storage {second_storage.name} has {second_storage.scanner_quantity}')
                print(f'Storage {self.name} has {self.copier_quantity}')
                print(f'Storage {second_storage.name} has {second_storage.copier_quantity}')
            elif action == 'q':
                # print(action)
                run = False
            else:
                print('somthing wrong')

        pass

class Technics:
    """ Класс оргтехники, общие характеристики, наименование, разрешение, скорость, цена"""

    def __init__(self, name, resolution, speed, price):
        self.name = name
        self.resolution = resolution
        self.speed = speed
        self.price = price


class Printer(Technics):
    def to_print(self):
        return f'This printer has resolution {self.resolution} dpi and print with speed {self.speed} page/min'


class Scanner(Technics):
    def to_scan(self):
        return f'This scanner has resolution {self.resolution} dpi and scan with speed {self.speed} page/min'


class Copier(Technics):
    def to_copier(self):
        return f'This copier has resolution {self.resolution} dpi and make copy with speed {self.speed} page/min'


# printer_1 = Printer('xerox', 1200, 20, 8790)
# printer_2 = Printer('hp', 1200, 20, 6490)
# printer_3 = Printer('canon', 600, 18, 9930)

# scaner_1 = Scaner('epson', 4800, 0, 9110)
# scaner_2 = Scaner('hp', 600, 0, 29520)
# scaner_3 = Scaner('canon', 2400, 0, 4180)

# copier_1 = Copier('xerox', 1200, 30, 11670)
# copier_2 = Copier('hp', 1200, 22, 15590)
# copier_3 = Copier('canon', 600, 22, 43570)

# print(printer_1.name)
print(Storage.__doc__)


main_storage = Storage('Moscow')
second_storage = Storage('Chelyabinsk')
print(Storage.to_storage.__doc__)
main_storage.to_storage
print(Storage.from_storage.__doc__)
main_storage.from_storage

# seventh task
print(' ')
print('seventh task')


class ComplexNumber:
    """ Сложение и вычитание происходят по правилу
    (a + bi) ± (c + di) = (a ± c) + (b ± d)i,
    а умножение — по правилу (a + bi) · (c + di) = (ac – bd) + (ad + bc)i """
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма z1 и z2 равна')
        return f'z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение z1 и z2 равно')
        return f'z = {self.a * other.a - (self.b * other.b)} + {(self.a * other.b + self.b * other.a)} * i'

    def __str__(self):
        return f'z = {self.a} + {self.b} * i'


z_1 = ComplexNumber(1, -2)
z_2 = ComplexNumber(3, 4)
print(z_1)
print(z_2)
print(z_1 + z_2)
print(z_1 * z_2)
