import os
import pickle
import pprint

class GameInfo:

	def __init__(self):
		'''Inicializacao do objeto'''

		self.data = {}
		self.load()

	def load(self):
		'''Carrega os dados do jogo'''
	
		if os.path.exists('gamedata.db'):
			f = open('gamedata.db', "rb")
			self.data = pickle.load(f)
			f.close()

	def save(self):
		'''Salva os dados do jogo'''

		f = open("gamedata.db", "wb")
		pickle.dump(self.data, f)
		f.close()


class Weapon:

	def __init__(self, name, damage):
		self.name = name
		self.damage = damage

	def __repr__(self):
		return "Weapon %s - Damage: %d" % (self.name, self.damage)

class Item:
	
	def __init__(self, name, type, damage, life):
		self.name = name
		self.type = type
		self.damage = damage
		self.life = life

	def __repr__(self):
		return "Item %s - Type: %s - Damage: %d - Life: %d" % (self.name, self.type, self.damage, self.life)


class Bag:

	def __init__(self, slots):
		self.slots = slots

	def __repr__(self):
		return "Bag com: %s" % self.slots

	def add_item(self, item):
		self.slots.append(item)

	def use_item(self, item_name):
		'''Recebe o nome do item, retorna ele e remove da bolsa'''

		for i in range(len(self.slots)):
			item = self.slots[i]

			if item.name == item_name:
				del(self.slots[i])
				return item

gi = GameInfo()

pp = pprint.PrettyPrinter(indent=4)

print("Dados do jogo:")

# Testa se existem dados para o jogo
if not gi.data:
	# Cria as armas iniciais
	gi.data['weapons'] = []
	
	# Cria a arma chamada Fists
	fists = Weapon('Fists', 3)
	gi.data['weapons'].append(fists)
	
	# Cria a arma chamada Sword
	sword = Weapon('Sword', 30)
	gi.data['weapons'].append(sword)

	# Cria os itens iniciais
	gi.data['bag'] = Bag([
		Item('Bread', 'heal', 10, 3),
		Item('Water', 'heal', 5, 1),
		Item('Flames', 'dmg', 20, 1),
	])

pp.pprint(gi.data)

def encounter(gi):
	print("Qual item quer utilizar?")
	item_name = input()
	item = gi.data['bag'].use_item(item_name)

	if item:
		print(repr(item))
	else:
		print("Item %s nao encontrado" % item_name)


encounter(gi)


gi.save()
