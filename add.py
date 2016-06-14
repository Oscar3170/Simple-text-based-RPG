from info import weapons, bag

def enemies_txt(area):
	if area==0:
		letters=('enemies=[\'Rat  03  10  35\', \'Pigeon  04  05  35\', \'Big Rat  04  15  65\']')
	elif area==1:
		letters=('enemies=[\'Amoeba  1  20  20\']')
	file=open('info.py','r')
	split_file=file.read().split('\n')
	split_file[2]=(letters)
	file=open('info.py', 'w')
	file.write('\n'.join(split_file))
	file.close()

def items_txt_add(new_item):
	_bag_=bag
	_bag_.append(new_item)
	file=open('info.py','r')
	split_file=file.read().split('\n')
	split_file[1]=('bag=[\''+'\', \''.join(_bag_)+'\']')
	file=open('info.py', 'w')
	file.write('\n'.join(split_file))
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
			_bag_.remove(chosen_item)
		else:
			joined_item='  '.join(split_item)
			_bag_[_bag_.index(chosen_item)]=joined_item
	else:
		split_item[3]=str(int(split_item[3])-1)
		if split_item[3]=='0':
			_bag_.remove(chosen_item)
		else:
			joined_item='  '.join(split_item)
			_bag_[_bag_.index(chosen_item)]=joined_item
	file=open('info.py','r')
	split_file=file.read().split('\n')
	split_file[1]=('bag=[\''+'\', \''.join(_bag_)+'\']')
	file=open('info.py', 'w')
	file.write('\n'.join(split_file))
	file.close()

def new_weapons(new_weapon):
	_weapons_=weapons
	_weapons_.append(new_weapon)
	file=open('info.py','r')
	split_file=file.read().split('\n')
	split_file[0]=('weapons=[\''+'\', \''.join(_weapons_)+'\']')
	file=open('info.py', 'w')
	file.write('\n'.join(split_file))
	file.close()

