import os
from random import randint

enemies=['Rat  03  10  40', 'Pigeon  07  05  45', 'Big Rat  08  20  65']
level=1
bag=['bread', 'water']
weapons=['Stick  999', 'Fists  5']
bonus=0
hp=20
defense=1
expe=0
expe_f=level*100*1.3


def encounter():
	gained_xp=1
	chance=randint(1,100)
	if chance<46:
		print('Something attacks you!')
		input()
		os.system('clear')
		battle_hp=hp
		enemie=enemies[randint(1,len(enemies))-1]
		e_lvl=level
		e_name=enemie.split('  ')[0]
		e_atk=int(int(enemie.split('  ')[1])*(1+level/9))
		e_hp=int(enemie.split('  ')[2])
		e_xp=int(enemie.split('  ')[3])
		print('ENEMIE: ' + e_name)
		print('LEVEL: ' + str(e_lvl))
		print('HEALTH: ' + str(e_hp))
		print('ATTACK: ' + str(e_atk))
		print('')
		while e_hp>0 and battle_hp>0:
			print('ACTIONS: Fight--Bag--Run')
			print('')
			action=input()
			while action.lower() !='fight' and action.lower() !='run' and action.lower()!='bag' and action.lower()!='0': 
				action=input()
			print('')
			if action=='0':
				break
			elif action.lower()=='fight':
				now_weapons = []
				for wea in weapons:
					now_weapons.append(wea.split('  ')[0])
				print('Weapon: ' + '--'.join(now_weapons))
				print('')
				dam_weapon=''
				weapon=input()
				print('')
				if weapon.lower()!='back':
					while dam_weapon=='':
						for con_weapon in weapons:
							if con_weapon.split('  ')[0].lower()==weapon.lower():
								dam_weapon=con_weapon.split('  ')[1]
						if dam_weapon=='':
							weapon=input()
					damage= int(dam_weapon)+(level/2)-(e_lvl/3)+randint(level-2,level+2)
					e_hp=e_hp - damage
					print(e_name +' has lost ' + str(int(damage))+ ' HP!')
					if e_hp<0:
						e_hp=0
					print('')
					print('')
			elif action.lower()=='run':
				run=randint(0,1)
				if run ==0:
					break
			if e_hp>0 and weapon.lower()!='back':
				print (e_name + ' attacks you!')
				print('')
				e_dmg = (e_atk-((level-e_lvl)/2)-defense)
				battle_hp=battle_hp-e_dmg
				print('You\'ve lost ' + str(int(e_dmg)) +' Hp!')	
				input()
				os.system('clear')
				if battle_hp>0:
					print(e_name+'\'s health: ' + str(int(e_hp)))
					print('')
					print('')
					print('Your health: ' + str(int(battle_hp)))
					print('')
				else:
					break
		if action.lower()=='run':
			print('You\'ve run away safely!')
		else:
			if battle_hp>0:
				print('The ' + e_name +' died!')
				gained_xp= e_xp*randint(1.1,1.999)
				print('You\'ve gained ' + str(int(gained_xp)) + ' xp!')
				return gained_xp
			elif battle_hp<=0:
				print('You died!')	
		input()
		os.system('clear')	


while True:
	print(str(level)+' '+str(defense)+' '+str(hp)+' '+str(int(expe))+' '+str(int(expe_f)))
	input()
	xp=encounter()
	if xp !=None:
		expe+=xp
	while expe>expe_f and level<50:
		level= level + 1
		defense= defense + 1
		hp= hp + 4
		expe_f=level*100*1.3
		if level==50:
			expe_f=0
			expe=0





























'''
def battle():
	print('RAT - 40HP')
	print('')
	print('Actions - Attack')


print('You have nothing')
print('something atacks you')
os.system('clear')


print('RAT - 40HP')
print('')
print('Actions - Attack')'''