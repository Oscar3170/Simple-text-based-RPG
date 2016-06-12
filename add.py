from list_bag import bag

def enemies_txt(area):
	file=open('list_enemies.py', 'w')
	if area==0:
		file.write('enemies=[\'Rat  03  10  35\', \'Pigeon  04  05  45\', \'Big Rat  04  20  65\', \'Amoeba  1  20  20\']')
		file.close()
	elif area==1:
		file.write('enemies=[\'Amoeba  1  20  20\', \'Amoeba  1  20  20\', \'Amoeba  1  20  20\']')
		file.close()
	else:
		file.write('enemies=[]')
		file.close()

def items_txt(new_item):
	_bag_=bag
	_bag_.append(new_item)
	file=open('list_bag.py', 'w')
	file.write('bag=[\''+'\', \''.join(_bag_)+'\']')

items_txt('Pinto  dmg  9999')
