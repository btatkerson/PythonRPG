'''
Just a test battle between two creatures
'''
from core.__core_constants import core_constants as cc
import os
import creature as cre

a = cc()
pc = cre.creature(True,"Frodo",a.CREATURECLASS.MONK,a.CREATURERACE.HALFLING,None,3,None,23,98,20,1,None,11,None,14,10,7,13,11,3,True)
npc = cre.creature(False,"Goblin",a.CREATURECLASS.FTR,a.CREATURERACE.GOBLINOID,None,.5,None,50,10,15,2,None,10,None,11,10,6,13,12,9,True)

print("\n\n---------------------------------------------------------------\n\n")

pc.stat_display()

print("\n\n---------------------------------------------------------------\n\n")

npc.stat_display()
print("\n\n---------------------------------------------------------------\n\n")


def attack(cre_a,cre_b):
    att_roll = cre_a.attack_roll()
    print(att_roll)
    for i in att_roll:
        if not cre_b.is_alive():
            break
        hit_or_miss = sum(i) >= cre_b.get_armor_class()
        if i[0] != 0:
            print(cre_a.get_name(),'rolls:',i[0],"|",sum(i),">=" if hit_or_miss else "<",cre_b.get_armor_class(),"| HIT!" if hit_or_miss else "| MISS!")
        else:
            print(cre_a.get_name(),"got a critical miss! No damage was done to", cre_b.get_name())
            break
        if hit_or_miss or i[0] == 20:
            damage = 0
            if i[0] == 20:
                print(cre_a.get_name(),"got a critical hit!")
                damage = cre_a.damage_roll(True)
            else:
                damage = cre_a.damage_roll()
            cre_b.set_current_hit_points(-1*damage)
            print(cre_a.get_name(),"did",damage,"damage to",cre_b.get_name())

def heal(cre_a):
        heal = sum(cre_a.d4()) + cre_a.mod_con()
        print(cre_a.get_name(),"healed",min(heal,cre_a.get_base_hit_points()-cre_a.get_current_hit_points()),"points!")
        cre_a.set_current_hit_points(heal)

while pc.is_alive() and npc.is_alive():
    input()
    os.system('clear')
    pc.stat_display()
    print("\n\n---------------------------------------------------------------\n\n")
    npc.stat_display()
    print("\n\n---------------------------------------------------------------\n\n")
    x = input("1. Attack\n2. Heal\n> ")
    if x == "1":
        attack(pc,npc)
    else:
        heal(pc) 
    
    if not npc.is_alive():
        break

    print("\n")

    attack_or_heal = sum(npc.d100())

    if npc.get_current_hit_points() is not npc.get_base_hit_points() and attack_or_heal >= int(npc.get_current_hit_points()*100/npc.get_base_hit_points()):
        heal(npc)
    else:
        attack(npc,pc)

input("\nPress Enter to continue")


os.system("clear")
if not npc.is_alive():
    print(pc.get_name(),"has killed",npc.get_name(),"!")
    pc.set_experience(npc)
    print('\n\n',pc.get_name(),"gained",pc.get_last_experience_earned(),"XP!\n\n")
    pc.stat_display()
else:
    print(npc.get_name(),"killed you!")
    print("\n\nGAME OVER")
