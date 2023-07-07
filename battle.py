
import random

class Battle:
	def __init__(self, description) -> None:
		self.description = description


class Battles(Battle):
	def __init__(self) -> None:
		super().__init__("Битва")
	
	"""Функция битвы с мобоми"""
	def encounter(self, entity, hero):
		self.hero = hero
		print("Вы встретили", entity.name)
		while entity.health > 0:
			print("Ваше здоровье:", self.hero.health)
			print("Здоровье", entity.name, entity.health)
			action = input("Выберите действие: 1. Атаковать, 2. Убежать")
			if action == "1":
				if self.hero.equipment.upgrade_attack() == None:
					damage = self.hero.attack - entity.defense
					if damage > 0:
						entity.health -= damage
						print("Вы нанесли", damage, "ед. урона", entity.name)
					else:
						print(entity.name, "защитился")
				else:
					damage = (self.hero.attack + self.hero.equipment.upgrade_attack()) - entity.defense
					if damage > 0:
						entity.health -= damage
						print("Вы нанесли", damage, "ед. урона", entity.name)
					else:
						print(entity.name, "защитился")
			elif action == "2":
				if random.randint(1, 2) == 1:
					return print("Вы убежали")
					
				else:
					print("Вы не смогли убежать")
			else:
				print("Некорректный ввод")
			
			if self.hero.equipment.upgrade_defence() == None:
				damage = entity.attack - self.hero.defense
				if damage > 0:
					self.hero.health -= damage
					print("Вам нанесли", damage, "ед. урона")
				else:
					print("Вы защитились")
			else:
				damage = entity.attack - (self.hero.defense + self.hero.equipment.upgrade_defence())
				if damage > 0:
					self.hero.health -= damage
					print("Вам нанесли", damage, "ед. урона")
				else:
					print("Вы защитились")
			
			if self.hero.health <= 0:
				return print("Вас убили")
		gold = random.randint(10, 20)
		self.hero.gold += gold
		print("Вы получили", gold, "золота")
		if entity.item == None:
			pass
		else:
			if entity.item.type_item == "ATA":
				self.hero.inventory.add_item(entity.item)
			elif entity.item.type_item == "DEF":
				self.hero.inventory.add_item(entity.item)
			elif entity.item.type_item == "CARCAS":
				self.hero.inventory.add_item(entity.item)
	
	"""Функция битвы с боссами"""
	def battle(self, boss, hero):
		self.hero = hero
		print("Вы бросили вызов", boss.name)
		while boss.health > 0:
			print("Ваше здоровье:", self.hero.health)
			print("Здоровье", boss.name, boss.health)
			action = input("Выберите действие: 1. Атаковать, 2. Убежать ")
			if action == "1":
				if self.hero.equipment.upgrade_attack() == None:
					damage = self.hero.attack - boss.defense
					if damage > 0:
						boss.health -= damage
						print("Вы нанесли", damage, "ед. урона", boss.name)
					else:
						print(boss.name, "защитился")
				else:
					damage = (self.hero.attack + self.hero.equipment.upgrade_attack()) - boss.defense
					if damage > 0:
						boss.health -= damage
						print("Вы нанесли", damage, "ед. урона", boss.name)
					else:
						print(boss.name, "защитился")
			elif action == "2":
				print("Вы не можете убежать от босса")
			else:
				print("Некорректый ввод")
			
			if self.hero.equipment.upgrade_defence() == None:
				damage = boss.attack - self.hero.defense
				if damage > 0:
					self.hero.health -= damage
					print("Вам нанесли", damage, "ед. урона")
				else:
					print("Вы защитились")
			else:
				damage = boss.attack - (self.hero.defense + self.hero.equipment.upgrade_defence())
				if damage > 0:
					self.hero.health -= damage
					print("Вам нанесли", damage, "ед. урона")
				else:
					print("Вы защитились")
			
			if self.hero.health <= 0:
				return print("Вас убил", boss.name)
		gold = random.randint(30, 40)
		self.hero.gold += gold
		print("Вы победили", boss.name, "и получили", gold, "золота")
		if boss.item.type_item == "ATA":
			self.hero.inventory.add_item(boss.item)
		elif boss.item.type_item == "DEF":
			self.hero.inventory.add_item(boss.item)