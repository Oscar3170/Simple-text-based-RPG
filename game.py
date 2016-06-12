import os
from random import randint
from add import enemies_txt
from fight import encounter
from info import level, bag, weapons, hp, expe, expe_f
from list_enemies import enemies


enemies_txt(1)
while True:
    print(str(level)+' '+str(hp)+' '+str(int(expe))+' '+str(int(expe_f)))
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
