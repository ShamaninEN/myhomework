# first task


print('first task')
class Matrix:
    def __init__(self, list_1):
        self.list_1 = list_1

    def __str__(self):
        new_list = []
        new_str = ''
        i = 0
        while i < len(self.list_1):
            my_str_1 = str(' '.join(map(str, self.list_1[i])))
            new_list.append(my_str_1)
            new_str = new_str + '\t' + ' '.join(my_str_1) + '\n'
            i += 1
        return str(new_str)

    def __add__(self, other):
        new_matrix = []
        i = 0
        while i < len(self.list_1):
            str_list = []
            j = 0
            while j < len(self.list_1[i]):
                str_list.append(self.list_1[i][j]+other.list_1[i][j])
                j += 1
            new_matrix.append(str_list)
            i += 1
        return Matrix(new_matrix)



my_matrix1 = Matrix([[3, 5, 3], [4, 5, 3], [5, 7, 3]])
my_matrix2 = Matrix([[4, 3, 1], [3, 3, 4], [3, 2, 1]])

print(my_matrix1)
print(my_matrix2)
print(my_matrix1 + my_matrix2)


# second task
print('second task')
from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def my_size(self, size):
        self.size = size
        print(f'Clothes name {self.size}')

    def __add__(self, other):
        total_value = self.value + other.value
        return total_value

class Coat(Clothes):

    def my_size(self, size):
        self.size = size
        self.value = self.size/6.5 + 0.5
        print(f'Clothes size {self.size}')
        print(f'Clothes value {self.value}')

class Suit(Clothes):

    def my_size(self, size):
        self.size = size
        self.value = 2 * self.size + 0.3
        print(f'Suit size {self.size}')
        print(f'Suit value {self.value}')




coat = Coat()
coat.my_size(44)

suit = Suit()
suit.my_size(44)

print(f'Total value: {coat + suit}')

# third task
print(' ')
print('third task')

class Cell:
    def __init__(self, number):
        self.number = int(number)
    def __add__(self, other):
        return Cell(self.number + other.number)
    def __sub__(self, other):
        if self.number > other.number:
            return Cell(self.number - other.number)
        else:
            print('you dont do that')

    def __mul__(self, other):
        return Cell(self.number * other.number)
    def __truediv__(self, other):
        if self.number > other.number:
            return Cell(self.number // other.number)
        else:
            print('you dont do that')
    def __str__(self):
        return f'new numbers into cell: {self.number}'
    def make_order(self, row):
        if self.number / row > 0:
            how_many_rows = self.number // row
            remainder_of_the_division = self.number % row
            row_str = str('*' * row + '\n') * how_many_rows + str('*' * remainder_of_the_division)
            return row_str
        else:
            print('you dont do that')


cell_1 = Cell('2')
cell_2 = Cell(7)
cell_3 = cell_1 + cell_2
cell_4 = cell_1 - cell_2
cell_4 = cell_3 - cell_1
cell_5 = cell_3 / cell_1
print(cell_3)
print(cell_4)
print(cell_5)
print(cell_2.make_order(3))

