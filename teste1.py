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

	def __init__(self):
		self.slots = []

	def __repr__(self):
		return "Bag com: %s" % self.slots

	def add_item(self, item):
		'''Adiciona um item na bag'''
		self.slots.append(item)

	def add_items(self, item_list):
		'''Adiciona uma lista de itens na bag'''
		for item in item_list:
			self.add_item(item)

	def use_item(self, item_name):
		'''Recebe o nome do item, retorna ele e remove da bolsa'''

		for i in range(len(self.slots)):
			item = self.slots[i]

			if item.name == item_name:
				del(self.slots[i])
				return item

class Player:

	def __init__(self, name):
		self.name = name
		self.bag = Bag()
		self.weapons = []
		self.hp = 29
		self.xp = 0

	def __repr__(self):
		return "Jogador %s - HP: %d - XP: %d" % (self.name, self.hp, self.xp)

	def use_item(self, item_name):
		'''Faz com que o jogador use um item'''

		item = self.bag.use_item(item_name)

		if not item:
			print("Item %s nao encontrado" % item_name)			
			return

		if item.type == "heal":
			self.hp += item.life
			print("%s usou %s e recuperou %s de life" % (self.name, item.name, item.life))
		else:
			raise Exception("Ainda nao sei como usar um item do tipo %s: %r" % (item.type, item))

gi = GameInfo()

pp = pprint.PrettyPrinter(indent=4)


# Testa se existem dados para o jogo
if not gi.data:

	print("Bem vindo ao RPG do Oscar")

	print("Qual eh o seu nome marujo?")
	name = input()

	player = Player(name)
	gi.data['player'] = player

	# Conjunto de armas iniciais
	player.weapons = [
		Weapon('Fists', 3),
		Weapon('Sword', 30)
	]

	# Cria os itens iniciais
	player.bag.add_items([
		Item('Bread', 'heal', 10, 3),
		Item('Water', 'heal', 5, 1),
		Item('Flames', 'dmg', 20, 1),
	])

print()
print("Situacao atual do jogo:")
pp.pprint(gi.data)

def encounter(gi):
	player = gi.data['player']

	print("Qual item quer utilizar?")
	item_name = input()

	player.use_item(item_name)



encounter(gi)



print()
print("Situacao final do jogo:")
pp.pprint(gi.data)
gi.save()

