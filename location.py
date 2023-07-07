
class Location:
    def __init__(self, description, entity=None) -> None:
        self.description = description
        self.entity = entity

    def has_entity(self):
        return self.entity is not None

    def get_entity(self):
        return self.entity

class Trade(Location):
    def __init__(self) -> None:
        super().__init__("Торговец")

    """Функция бродячего торговца"""
    def trade(self, hero):
        self.hero = hero
        print("Вы встретили кота бабушки и дедушки")
        print("Здраствуй Ваня, я кот-торговец")
        print("У меня есть в продаже зелье здоровье за 5 золота")
        while True:
            print("У вас", self.hero.gold, "золота")
            action = input("Хотите купить зелье здоровья ? 1. Да, 2. Нет ")
            if action == "1":
                if self.hero.gold >= 15:
                    self.hero.gold -= 15
                    self.hero.health += 35
                    print("Вы купили зелье здоровья")
                else:
                    print("У вас не достаточно золота")
            elif action != "2":
                print("Некорректый ввод")
            elif action == "2":
                break


class City(Location):
    def __init__(self) -> None:
        super().__init__("Город")
    
    
    """Функция городского торговца"""
    def trade1(self, hero):
        self.hero = hero
        print("Вы посетили торговца")
        print("Привет парень покупать или продовать?")
        while True:
            vib = input("Выберете действие: 1.Покупать 2.Продовать 3.Закончить торговлю")
            if vib == '1':
                while True:
                    print("У вас", self.hero.gold, "золота")
                    action = input("Выберете что хотите купить: 1.Малое зелье здоровья, 2.Среднее зелье здоровья,"
                                   "\n3.Большое зелье здоровья. 4.Закончить Покупки ")
                    if action == '1':
                        if self.hero.gold >= 5:
                            self.hero.gold -= 5
                            self.hero.health += 20
                            print("Вы купили зелье здоровья")
                        else:
                            print("У вас не достаточно золота")
                    elif action == '2':
                        if self.hero.gold >= 13:
                            self.hero.gold -= 13
                            self.hero.health += 25
                            print("Вы купили зелье здоровья")
                        else:
                            print("У вас не достаточно золота")
                    elif action == '3':
                        if self.hero.gold >= 25:
                            self.hero.gold -= 25
                            self.hero.health += 35
                            print("Вы купили зелье здоровья")
                        else:
                            print("У вас не достаточно золота")
                    elif action == '4':
                        break
                    else:
                        print("Некоректный ввод")
            elif vib == '2':
                    while True:
                        self.hero.inventory.Print_inventory()
                        vib = input("Напишите название того что продать из инвенторя или "
                                    "введите 'выход' что бы закончить покупки ").title()
                        s = self.hero.inventory.remove_item(vib)
                        if s != None:
                            self.hero.gold += s.price
                            self.hero.inventory.items.remove(s)
                        elif vib == "Выход":
                            break
                        else:
                            print("Такого в инвентаре нет")
            elif vib == '3':
                break
            else:
                print("Некоректный ввод")

    """Функция городского кузнеца"""
    def blacksmith(self, hero):
        self.hero = hero
        print("Вы посетили кузница")
        print("Парень я не продою оружие только улучшаю")
        while True:
            self.hero.inventory.Print_inventory()
            vib = input("Напишите название того что улучшить из инвенторя или введите 'выход' что бы выйти ").title()
            s = self.hero.inventory.remove_item(vib)
            if s != None:
                while True:
                    print("У вас", self.hero.gold, "золота")
                    inv = input("Выбери какое улучшение ставить: 1.Малое усилиние 50 золота 2.Среднее усилиние 90 золота "
                                "\n                              3.Большое усилиние 150 золота 4.Закончить усиления ")
                    if inv == '1':
                        if self.hero.gold >= 30:
                            self.hero.gold -= 25
                            s.mod += 4
                            print("Вам установили малое усилиние")
                    elif inv == '2':
                        if self.hero.gold >= 60:
                            self.hero.gold -= 40
                            s.mod += 8
                            print("Вам установили средние усилиние")
                    elif inv == '3':
                        if self.hero.gold >= 90:
                            self.hero.gold -= 90
                            s.mod += 12
                            print("Вам установили большое усилиние")
                    elif inv == '4':
                        break
                    else:
                        print("Некоректный ввод")
            elif vib == 'Выход':
                break
            else:
                print("Такого в инвентаре нет")