# second task
print('second task')

class Road:
    _length = 5000
    _width = 20

    def count_how_many(self, length = 5000, width = 20):
        self._length = length
        self._width = width
        print(f'{length * width * 25 * 1/1000} t')

road_1 = Road()
road_1.count_how_many(int(input('Enter ligth: ')), int(input('Enter width: ')))
print(road_1._length)

# third task
print(' ')
print('third task')


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        _income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(f'Full name: {self.name} {self.surname}')

    def get_total_income(self):
        print(f'Total income: : {int(self.wage) + int(self.bonus)}')


worker_1 = Position('Vasya', 'Ivanov', 'accounter', 25000, 10000)
worker_1.get_full_name()
worker_1.get_total_income()

# fourth task
print(' ')
print('fourth task')

class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print('Car is driving')
    def stop(self):
        print('Car stop')
    def turn(self, direction):
        print(f'Car turn {direction}')
    def show_speed(self):
        print(f'Current speed: {self.speed}')


class TownCar(Car):
    type = 'town car'
    def show_speed(self):
        if self.speed > 60:
            print('You drive too fast')
        print(f'Current speed: {self.speed}')

class SportCar(Car):
    type = 'sport car'

class WorkCar(Car):
    type = 'work car'

    def show_speed(self):
        if self.speed > 40:
            print('You drive too fast')
        print(f'Current speed: {self.speed}')

class PoliceCar(Car):
        type = 'police car'
        is_police = True

police_car_1 = PoliceCar(200, 'Red', 'volvo')
print(f'This is a {police_car_1.color} {police_car_1.type},\ncurrent speed: {police_car_1.speed},\nauto name: {police_car_1.name}')
police_car_1.go()
police_car_1.stop()
police_car_1.turn('left')
police_car_1.show_speed()

work_car_1 = WorkCar(200, 'Blue', 'pegeout')
print(f'This is a {work_car_1.color} {work_car_1.type},\ncurrent speed: {work_car_1.speed},\nauto name: {work_car_1.name}')
work_car_1.go()
work_car_1.stop()
work_car_1.turn('right')
work_car_1.show_speed()

sport_car_1 = SportCar(200, 'white', 'bmw')
print(f'This is a {sport_car_1.color} {sport_car_1.type},\ncurrent speed: {sport_car_1.speed},\nauto name: {sport_car_1.name}')
sport_car_1.go()
sport_car_1.stop()
sport_car_1.turn('on')
sport_car_1.show_speed()

town_car_1 = TownCar(200, 'green', 'audi')
print(f'This is a {town_car_1.color} {town_car_1.type},\ncurrent speed: {town_car_1.speed},\nauto name: {town_car_1.name}')
town_car_1.go()
town_car_1.stop()
town_car_1.turn('away')
town_car_1.show_speed()


# fifth task
print(' ')
print('fifth task')

class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print(f'{self.title} отрисовки.')

class Pencil(Stationery):
    def draw(self):
        print(f'{self.title} чертит')

class Pen(Stationery):
    def draw(self):
        print(f'{self.title} пишет')

class Handle(Stationery):
    def draw(self):
        print(f'{self.title} подчеркивает')

pen = Pen('Ручка')
pen.draw()


pensil = Pencil('Карандаш')
pensil.draw()


handler = Handle('Маркер')
handler.draw()
