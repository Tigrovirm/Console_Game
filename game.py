import time
import random

from character import Hero, Banny, Bear, Kolobok, Volkolak, Bee, Box, Wolf, Goblin, Portal
from location import Location, City, Trade
from battle import Battles

class Game:
    def __init__(self) -> None:
        self.hero = Hero()
        self.city = City()
        self.battles = Battles()
        self.portal = Portal()
        self.loc_trade = Trade()
        self.locations = [
            Location("Дом") ,#0
            Location(self.city.description),#1
            Location("Выход из города"),#2
            Location("Поля"),#3
            Location("Опушка Леса"),#4
            Location("Лес"),#5
            Location("Чаща"),#6
            Location("Поляна посреди Леса"),#7
            Location("Одинокое дерево"),#8
            Location("Волчья нора"),#9
            Location("Ручей"),#10
            Location("Предгорье"),#11
            Location("Перевал"),#12
            Location("Горный Лес"),#13
            Location("Територия Медведя"),#14
            Location("Спуск с Горы"),#15
            Location("Вход в Темный Лес"),#16
            Location("Темный Лес"),#17
            Location("Вход в Темную пешеру"),#18
            Location("Темная Пешера"),#19
        ]
    """Функция Старта Игры"""
    def start(self):
        self.hero = Hero()
        print("Вы проснулись и обнаружили, что вашу бабушку и дедушку похитил злой Колобок")
        time.sleep(0.5)
        print("Вы решили идти на поиски и спасение свои родных!")
        time.sleep(0.5)
        print("Колобок расположился на востоке, вам предстоит прйоти через множество опасных мест.")
        time.sleep(0.5)
        print("Да начнём наше путишествие!")
        time.sleep(3)
        self.current_location = 0
        self.next_location()
        
    def next_location(self):
        location = self.locations[self.current_location]
        print("!! Вы находитесь в", location.description, "!!")
        if location.has_entity():
            self.battles.encounter(location.get_entity(), self.hero)
        else:
            self.check_location()
    
    """Функция вызова Привязка локации к порталу"""
    def beacon(self):
        self.portal.beacon(self.current_location)

    """Функция работы портала"""
    def portals(self):
        if self.current_location != 1:
            self.current_location = 1
            self.next_location()
        else:
            beac = self.portal.beacon_location()
            if len(self.portal.beacons) > 0:
                if beac != 1:
                    self.current_location = beac
                    self.portal.beacons.remove(beac)
                    self.next_location()
            else:
                print("У вас не установлен Портал")
    
    """Функция действий после конца игры"""
    def validate_location(self):
        time.sleep(3)
        next_location = self.current_location + 1
        if self.hero.health <= 0:
            print("Вы Погибли!")
            while True:
                Choice = input("Выберете действие: 1.Закончить игру 2.Начать сначала ")
                if Choice == '1':
                    exit()
                elif Choice == '2':
                    self.start()
                else:
                    print("некоректный ввод")
        else:
            if self.current_location == 19:
                print("Вы спасли своих родных и вернулись домой")
                while True:
                    Choice = input("Выберете действие: 1.Закончить игру 2.Начать сначала ")
                    if Choice == '1':
                        exit()
                    elif Choice == '2':
                        self.start()
                    else:
                        print("некоректный ввод")
            else:
                time.sleep(1)
                self.current_location = next_location
                self.next_location()

    """Проверка Локации"""
    def check_location(self):
        if self.hero.health <= 0:
            self.validate_location()
        if self.current_location == 5:
            time.sleep(2)
            self.battles.battle(Banny(), self.hero)
            self.validate_location()
        elif self.current_location == 9:
            time.sleep(2)
            self.battles.battle(Volkolak(), self.hero)
            self.validate_location()
        elif self.current_location == 14:
            time.sleep(2)
            self.battles.battle(Bear(), self.hero)
            self.validate_location()
        elif self.current_location == 19:
            print("Вы пришли к пешере Колобка")
            time.sleep(2)
            self.battles.battle(Kolobok(), self.hero)
            self.validate_location()
        else:
            self.scan_location()
    
    """Функция действий на простых локациях"""
    def scan_location(self):
        while True:
            if self.current_location != 1:
                action = input("Выберете действия: 1. Осмотреться, 2.Идти Дальше, "
                               "3.Инвентарь 4.Установить Портал ")
                if action == '1':
                    if self.current_location == 0:
                        self.battles.encounter(Box(), self.hero)
                        self.validate_location()
                    else:
                        self.generate_random_encounter()
                elif action == '2':
                    self.validate_location()
                elif action == '3':
                    self.hero.inventory.Print_inventory()
                    self.hero.inventory.invent(self.hero)
                elif action == '4':
                    if len(self.portal.beacons) > 0:
                        self.portal.delete_beacon()
                        self.beacon()
                        self.portals()
                    else:
                        self.beacon()
                        self.portals()
                else:
                    print("Не коректный ввод")
            else:
                action = input("Выберете действия: 1. Осмотреться, 2.Идти Дальше, "
                               "3.Инвентарь 4.Портал обратно к маяку ")
                if action == '1':
                    print("Вы находите торговца и кузница")
                    while True:
                        vib = input("Выберете к кому подойти: 1.Торговец 2.Кузнец 3.Выйти из города ")
                        if vib == '1':
                            self.city.trade1(self.hero)
                        elif vib == '2':
                            print(self.hero.inventory.items)
                            self.city.blacksmith(self.hero)
                        elif vib == '3':
                            break
                        else:
                            print("Некоректный Ввод")
                elif action == '2':
                    self.validate_location()
                elif action == '3':
                    self.hero.inventory.Print_inventory()
                    print("У вас", self.hero.gold, "золота")
                    self.hero.inventory.invent(self.hero)
                elif action == '4':
                    print(len(self.portal.beacons))
                    self.portals()
                else:
                    print("Некоректный ввод")

    """Функция генератора событий"""
    def generate_random_encounter(self):
        encounter = random.randint(1, 3)
        if encounter == 1:
            self.loc_trade.trade(self.hero)
            self.validate_location()
        elif encounter == 2:
            if self.current_location == 2 or self.current_location == 3 or self.current_location == 4:
                self.battles.encounter(Bee(), self.hero)
                self.validate_location()
            elif self.current_location == 6 or self.current_location == 7 or self.current_location == 8:
                self.battles.encounter(Wolf(), self.hero)
                self.validate_location()
            else:
                self.battles.encounter(Goblin(), self.hero)
                self.validate_location()
        else:
            print("Ничего не происходит идем дальше!")
            self.validate_location()
