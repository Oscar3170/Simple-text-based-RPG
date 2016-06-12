import os
from random import randint

enemies=['Rat  03  10  35', 'Pigeon  04  05  45', 'Big Rat  04  20  65', 'Amoeba  1  20  20']
level=1
bag=['Bread  heal  10', 'Water  heal  5', 'Flames  dmg  20', 'X Defense  boost  defense  3', 'X Attack  boost  atk  2']
weapons=['Newton\'s Flaming Laser Sword  999', 'Fists  3', 'Slap  1']
bonus=0
hp=10
defense=0
expe=0
expe_f=level*100*1.3


def encounter():
<<<<<<< HEAD
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
		e_hp=int(enemie.split('  ')[2])*level/2
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


fkjbrfjkbrekjhew
ewrjhebwtherbtjhber
wberjkbtkejwrbtkejrwbt
wertewraSDASD
ASDFASDFASFASDF
ASDFASDFASFASDF
dsfasd
Fistsdaf
sdaf
asd
for ASDFASDFASFASDFas
dsfasdsdf
ASDFASDFASFASDFasasdf
sd
for sdaf
Fistsdafdf
asd
for ASDFASDFASFASDFasasdfasdf
asd
for sdaf
for in 
for x in xrange(1,10):
	pass:
 	pass in xrange(1,10):
 	pass in xrange(1,10):
 	pass in xrange(1,10):
	pass










=======
    chance=randint(1,100)
    if chance<46:
        weapon=''
        chosen_item=''
        _run=False
        print('Something attacks you!')
        input()
        os.system('clear')
        battle_hp=hp
        battle_defense=defense
        battle_bonus=bonus
        enemie=enemies[randint(1,len(enemies))-1]
        e_lvl=level
        e_name=enemie.split('  ')[0]
        e_atk=int(int(enemie.split('  ')[1])*(1+level/6))
        e_hp=int(enemie.split('  ')[2])
        e_xp=int(enemie.split('  ')[3])
        print(e_name)
        print('HP: ' + str(e_hp))
        print('ATK: ' + str(e_atk))
        print('')
        while e_hp>0 and battle_hp>0:
            if weapon.lower() =='back' or chosen_item.lower()=='back':
            	print('')
            print('Actions: Fight--Bag--Run')
            weapon=''
            chosen_item=''
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
                print('Weapons: ' + '--'.join(now_weapons))
                print('')
                dam_weapon=''
                weapon=input()
                if weapon.lower()=='nfls':
                	weapon='Newton\'s Flaming Laser Sword'
                while weapon.lower()!='back':
                    while dam_weapon=='':
                        for con_weapon in weapons:
                            if con_weapon.split('  ')[0].lower()==weapon.lower():
                                dam_weapon=con_weapon.split('  ')[1]
                        if dam_weapon=='':
                            weapon=input()
                            if weapon.lower()=='back':
                            	break
                    if weapon.lower()=='back':
                        break
                    print('')
                    damage= int(dam_weapon)+(level/2*battle_bonus)+randint(0,2)
                    e_hp=e_hp - (damage)
                    print(e_name +' has lost ' + str(int(damage))+ ' HP!')
                    if e_hp<0:
                        e_hp=0
                    print('')
                    print('')
                    break
            elif action.lower()=='run':
                run=randint(0,1)
                if run ==0:
                    _run=True
                    break
                else:
                	print('Couldn\'t get away safely!')
                	print('')
            elif action.lower()=='bag':
            	items_name=[]
            	for item in bag:
            		items_name.append(item.split('  ')[0])
            	print('Items: ' + '--'.join(items_name))
            	dam_item=''
            	print('')
            	chosen_item=input()
            	while chosen_item.lower()!='back':
                    while dam_item=='':
                        for con_item in bag:
                            if chosen_item.lower() in con_item.lower():
                                dam_item=con_item
                        if dam_item=='':
                            chosen_item=input() 
                            if chosen_item.lower()=='back':
                            	break
                    if chosen_item.lower()=='back':
                        break 
                    print('')
                    item_function=dam_item.split('  ')
                    if item_function[1]=='heal':
                    	battle_hp+=int(item_function[2])
                    	print('The '+item_function[0]+ ' healed you for ' + item_function[2] + ' Hp!')
                    elif item_function[1]=='dmg':
                    	e_hp-=int(item_function[2])
                    	print('The '+item_function[0]+ ' dealt '+item_function[2]+' damage to the '+e_name+'!')
                    elif item_function[1]=='boost':
                    	if item_function[2]=='defense':
                    		battle_defense+=int(item_function[3])
                    		print('The '+item_function[0]+' boosted your defense to '+battle_defense+'!')
                    	elif item_function[2]=='atk':
                    		battle_bonus+=int(item_function[3])
                    		print('The '+item_function[0]+' boosted your attack to '+battle_bonus+'!')
                    print('')
                    print('')
                    break	
            if e_hp>0 and weapon.lower()!='back' and chosen_item.lower()!='back':
                print (e_name + ' attacks you!')
                print('')
                e_dmg = (e_atk - battle_defense*(level/2))
                battle_hp=battle_hp-e_dmg
                print('You\'ve lost ' + str(int(e_dmg)) +' Hp!')
                input()
                if battle_hp>0:
                    os.system('clear')
                    print(e_name+'\'s health: ' + str(int(e_hp)))
                    print('')
                    print('')
                    print('Your health: ' + str(int(battle_hp)))
                    print('')
                else:
                    break
        if _run:
            print('You\'ve run away safely!')
            input()
            os.system('clear')
        else:
            if battle_hp>0:
                if e_name=='Amoeba':
                    print('The ' + e_name + ' was fried')
                else:
                    print('The ' + e_name +' died!')
                gained_xp= e_xp
                print('You\'ve gained ' + str(int(gained_xp)) + ' xp!')
                input()
                os.system('clear')
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
    while expe>=expe_f and level<50:
        level= level + 1
        hp= hp + 4
        expe_f=level*100*1.3
        if level==50:
            expe_f=0
            expe=0
>>>>>>> df394a389ed1a77503468a1aa8af696c2cd73971


















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