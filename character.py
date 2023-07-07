
class Hero:
    def __init__(self) -> None:
        self.health = 100
        self.attack = 10
        self.defense = 5
        self.gold = 20
        self.inventory = Inventory()
        self.equipment = Equipment()

"""Портал"""
class Portal:
    def __init__(self) -> None:
        self.beacons = []
    
    """Функция привязки локации к порталу"""
    def beacon(self, beacon):
        self.beacons.append(beacon)
    
    """Функция удаления прявязки локации к порталу"""
    def delete_beacon(self):
        self.beacons.clear()
    
    """Функция определеня какая локация привазана к порталу"""
    def beacon_location(self):
        for i in self.beacons:
            return i

"""Экипировка"""
class Equipment:
    def __init__(self) -> None:
        self.equipments = []
    
    """Функция экипировки прдметов"""
    def add_equipment(self, item):
        if len(self.equipments) >= 0:
            for i in self.equipments:
                if i.type_item == "DEF" and item.type_item == "DEF":
                    print("Вы уже экипорованы в зашите")
                    break
                elif i.type_item == "ATA" and item.type_item == "ATA":
                    print("Вы уже экипорованы в атаке")
                    break
            else:
                self.equipments.append(item)
    
    """Функция снятия надетого предмета"""
    def remove_equipment(self, eqp):
        for i in self.equipments:
            if i.name == eqp:
                return i
    
    """Функция передачи характеристики атаки"""
    def upgrade_attack(self):
        for i in self.equipments:
            if i.type_item == "ATA":
                return i.mod

    """Функция передачи характеристики Зашиты"""
    def upgrade_defence(self):
        for i in self.equipments:
            if i.type_item == "DEF":
                return i.mod
    
    """Функция для показа Экипировки"""
    def print_equipment(self):
        print("__Экипировка__")
        count = 0
        for item in self.equipments:
            print(count, item.name, item.description)
            count += 1

"""Инвентарь"""
class Inventory:
    def __init__(self) -> None:
        self.items = []
    
    """Функция добовления предметов в инвентарь"""
    def add_item(self, item):
        self.items.append(item)
    
    """Функция удаления предмета из инвентаря"""
    def remove_item(self, vib):
        for i in self.items:
            if i.name == vib:
                return i

    """Функция для показа Инвентаря"""
    def Print_inventory(self):
        print("__Инвентарь__")
        count = 0
        for item in self.items:
            print(count, item.name, item.description, item.mod)
            count += 1
    
    """Функция действий с инвентарем и экипировкой"""
    def invent(self, hero):
        self.hero = hero
        while True:
            action = input(
                "Выберете действия: 1.надеть предмет 2.Снять предмет 3.Вернуться к основным действиям ")
            if action == '1':
                self.hero.inventory.Print_inventory()
                try:
                    vib = input("Выберет название предмет для оснашения ").title()
                    s = self.hero.inventory.remove_item(vib)
                    self.hero.equipment.add_equipment(s)
                    self.hero.inventory.items.remove(s)
                except (AttributeError, TypeError, ValueError):
                    print("Не коректный ввод")
            elif action == '2':
                self.hero.equipment.print_equipment()
                try:
                    eqp = input("Выберет название предмет для снятия ").title()
                    s = self.hero.equipment.remove_equipment(eqp)
                
                    self.hero.inventory.add_item(s)
                    self.hero.equipment.equipments.remove(s)
                except (AttributeError, TypeError, ValueError):
                    print("Не коректный ввод")
            elif action == '3':
                break
            else:
                print("Не коректный ввод")

"""Класс предмет"""
class Item:
    def __init__(self, name, description, mod, price, type_item) -> None:
        self.name = name
        self.description = description
        self.mod = mod
        self.price = price
        self.type_item = type_item

"""Класс Моб"""
class Mob:
    def __init__(self, name, health, attack, defense) -> None:
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense


class Bee(Mob):
    def __init__(self, ) -> None:
        super().__init__("Пчела", 5, 5, 3)
        self.item = None

class Wolf(Mob):
    def __init__(self) -> None:
        super().__init__("Волк", 15, 15, 5)
        self.item = Item("Труп Волка", "Добытая вами Туша Волка", 0, 20, "CARCAS")

class Goblin(Mob):
    def __init__(self) -> None:
        super().__init__("Гоблин", 25, 20, 8)
        self.item = Item("Труп Гоблина", "Добытая вами Туша Гоблина", 0, 45, "CARCAS")

class Box(Mob):
    def __init__(self) -> None:
        super().__init__("Сундук", 0, 0, 0)
        self.item = Item("Палка", "Ваш воображаемый меч", 5, 5, "ATA")

"""Класс Босс"""
class Boss:
    def __init__(self, name, health, attack, defense) -> None:
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense


class Banny(Boss):
    def __init__(self, ) -> None:
        super().__init__("Заяц", 30, 7, 2)
        self.item = Item("Кинжал", "Старый кинжал", 10, 25, "ATA")


class Volkolak(Boss):
    def __init__(self) -> None:
        super().__init__("Волколак", 40, 10, 5)
        self.item = Item("Кожанная Броня", "Броня из Волчей Кожи", 15, 50, "DEF")


class Bear(Boss):
    def __init__(self) -> None:
        super().__init__("Темный Медведь", 60, 20, 10)
        self.item = Item("Кольчуга", "Предедушему владельцу она не помогла, может вам поможет.", 19, 80, "DEF")


class Kolobok(Boss):
    def __init__(self) -> None:
        super().__init__("Колобок", 130, 30, 15)
        self.item = None