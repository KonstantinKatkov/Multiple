# Создайте родительский(базовый) класс Vehicle, который имеет свойство vehicle_type = "none"
# Создайте родительский(базовый) класс Car, который имеет свойство price = 1000000
# и функцию def horse_powers, которая возвращает количество лошидиных сил для автомобиля
# Создайте наследника класса Car и Vehicle - класс Nissan и переопределите свойство price и vehicle_type,
# а также переопределите функцию horse_powers
# Создайте экзмепляр класса Nissan и распечайте через функцию print vehicle_type, price


class Vechicle:
    def __init__(self, vechicle_type, price, powers):
        self.vechicle_type = vechicle_type
        self.vechicle_type = 'none'
        super().__init__(price)
        super().horse_powers(price)


class Car:
    def __init__(self, price):
        self.price = price
        self.price = 1000000


    def horse_powers(self, powers):
        self.powers = powers
        print(f'Мощность автомобиля {self.powers} л/с')


class Nissan(Vechicle, Car):
    def __init__(self, vechicle_type, price, powers):
        super().__init__(vechicle_type, price, powers)
        self.vechicle_type = vechicle_type
        self.price = price
        print(f'Тип автомобиля - {self.vechicle_type}, стоимость - {self.price} руб.')



print(Nissan.mro())
print()
car = Nissan("Легковой", 2000000, 200)