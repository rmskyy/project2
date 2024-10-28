import random
from multiprocessing.managers import public_methods
from random import randint


class Sneaker:
    def __init__(self, brand, size, price):
        self.brand = brand
        self.size = size
        self.price = price

class SneakerStore:
    def __init__(self):
        self.stock = []
    def add_sneaker(self, brand, size, price):
        sneaker = Sneaker(brand, size, price)
        self.stock.append(sneaker)
        print("Был добавлен :" + brand + ' ' + str(price) + ' ' + str(size))
    def display_stock(self):
        if self.stock == []:
            print("На складе нету ничего")
        else:
            print("Вот кроссы:")
            for sneaker in self.stock:
                print(sneaker.brand, sneaker.size, sneaker.price)
    def buy_sneaker(self, brand, size, money):
        for sneaker in self.stock:
            if sneaker.brand == brand and sneaker.size == size:
                if(money >= sneaker.price):
                    self.stock.remove(sneaker)
                    print("Ты купил:" + brand + ' ' + str(size))
                    return
                else:
                    print("не хватает на " + brand)
                    return
        print("Такого бренда нет в наличии")

class Human:
    def __init__(self, money):
        self.money = money


    def earn_money(self):
        money = random.randint(1000, 15000)
        print("заработано ", money)
        return money

store = SneakerStore()
store.add_sneaker('Nike', 27, 20000)
store.add_sneaker('Adas', 27, 2000)
store.display_stock()

humanLife = Human(0)
humanLife.money = humanLife.earn_money()
humanLife.money = humanLife.earn_money()
store.buy_sneaker('Nike', 27, humanLife.money)
store.buy_sneaker('Adas', 27, humanLife.money)
