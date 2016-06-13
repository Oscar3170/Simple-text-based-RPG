from list_bag import bag
from list_enemies import enemies
from current_area import area

def enemies_txt():
	file=open('list_enemies.py', 'r')
	red=file.read()
	if area==0:
		letters=('enemies=[\'Rat  03  10  35\', \'Pigeon  04  05  45\', \'Big Rat  04  15  65\']')
	elif area==1:
		letters=('enemies=[\'Amoeba  1  20  20\']')
	if letters != red:
		file=open('list_enemies.py', 'w')
		file.write(letters)
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
	file=open('list_bag.py', 'w')
	file.write('bag=[\''+'\', \''.join(_bag_)+'\']')
	file.close()

def change_area(now_area):
	changed_area='area='+str(now_area)
	file=open('current_area.py', 'w')
	file.write(changed_area)
	file.close
