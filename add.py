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

def items_txt_add(new_item):
	_bag_=bag
	_bag_.append(new_item)
	file=open('list_bag.py', 'w')
	file.write('bag=[\''+'\', \''.join(_bag_)+'\']')
	file.close()

def items_txt_rmv(item):
	_bag_= bag
	for the_item in _bag_:
		if item == the_item.split('  ')[0]:
			chosen_item=the_item
			split_item=chosen_item.split('  ')
	if split_item[1]=='boost':
		split_item[4]=(str(int(split_item[4])-1))
		if split_item[4]=='0':
			_bag_.remove(the_item)
		else:
			joined_item='  '.join(split_item)
			_bag_[_bag_.index(chosen_item)]=joined_item
	else:
		split_item[3]=str(int(split_item[3])-1)
		if split_item[3]=='0':
			_bag_.remove(the_item)
		else:
			joined_item='  '.join(split_item)
			_bag_[_bag_.index(chosen_item)]=joined_item
	file=open('list_bag.py', 'w')
	file.write('bag=[\''+'\', \''.join(_bag_)+'\']')
	file.close()

			

items_txt_rmv('Bread')