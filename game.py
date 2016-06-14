import os
from random import randint
from add import enemies_txt, items_txt_add
from fight import encounter
from info import level, weapons, hp, expe, expe_f, bag


while True:
    print("Level: %s  HP: %s  XP: %s  XP_f: %s" % (level, hp, expe, expe_f))
    print(str(level)+' '+str(hp)+' '+str(int(expe))+' '+str(int(expe_f)))
    enemies_txt(1)
    input()
    xp=encounter()
    if xp !=None and level<50:
        expe+=float(xp)
    while expe>=expe_f and level<50:
        level= level + 1
        hp= hp + 4
        expe_f=level**3*(100+100/3)
        if level==50:
            expe_f=0
            expe=0