import os
from random import randint
from add import enemies_txt, items_txt_add
from fight import encounter
from info import level, weapons, hp, expe, expe_f
from list_bag import bag
from list_enemies import enemies


while True:
    print(str(level)+' '+str(hp)+' '+str(int(expe))+' '+str(int(expe_f)))
    input()
    xp=encounter()
    if xp !=None and level<50:
        expe+=xp
    while expe>=expe_f and level<50:
        level= level + 1
        hp= hp + 4
        expe_f=level*100*1.3
        if level==50:
            expe_f=0
            expe=0