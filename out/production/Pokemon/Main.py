# -*- coding:utf-8 -*-
import random
import time

from Monster import Monster
from Rucksack import Rucksack

monster = Monster("You", "Relaxo", 100, [["A1", 2, 5], ["A2", 6, 2], ["A3", 2, 10], ["A4", 2, 15]])
monster1 = Monster("Auto", "Glurak", 100, [["A1", 23, 5], ["A2", 66, 2], ["A3", 12, 10], ["A4", 5, 15]])
monster2 = Monster("You", "Gengar", 100, [["A1", 2, 5], ["A2", 6, 2], ["A3", 2, 10], ["A4", 2, 15]])
monster3 = Monster("You", "Quajutsu", 100, [["A1", 2, 5], ["A2", 6, 2], ["A3", 2, 10], ["A4", 2, 15]])
monster4 = Monster("You", "Luxtra", 100, [["A1", 2, 5], ["A2", 6, 2], ["A3", 2, 10], ["A4", 2, 15]])
monster5 = Monster("You", "Lohgock", 100, [["A1", 2, 5], ["A2", 6, 2], ["A3", 2, 10], ["A4", 2, 15]])
monster6 = Monster("Auto", "Dev1", 100, [["A1", 2, 5], ["A2", 6, 2], ["A3", 2, 10], ["A4", 2, 15]])
monster7 = Monster("Auto", "Dev2", 100, [["A1", 2, 5], ["A2", 6, 2], ["A3", 2, 10], ["A4", 2, 15]])
monster8 = Monster("Auto", "Dev3", 100, [["A1", 2, 5], ["A2", 6, 2], ["A3", 2, 10], ["A4", 2, 15]])
monster9 = Monster("Auto", "Dev4", 100, [["A1", 2, 5], ["A2", 6, 2], ["A3", 2, 10], ["A4", 2, 15]])
monster10 = Monster("Auto", "Dev5", 100, [["A1", 2, 5], ["A2", 6, 2], ["A3", 2, 10], ["A4", 2, 15]])
monster11 = Monster("Auto", "Dev6", 100, [["A1", 2, 5], ["A2", 6, 2], ["A3", 2, 10], ["A4", 2, 15]])


Pokeballs = [monster, monster1, monster2,
             monster3, monster4, monster5]

rucksack = Rucksack("You", Pokeballs)

rucksack.checkifAlive()



runde = 1
Gameloop = True
Bag = True
Attacks = True
menu = True
player = True


while Gameloop:
    #NPC
    print("______________________________________________")

    print("Player: " + monster1.trainer)
    print("Pokemon: " + monster1.name + "                 current HP: " + str(monster1.life_points))
    monster1.showAttacks()
    #option = input(random.randrange{})  # choose Attack

    damage = monster1.chooseAttack(random.randrange(1, 5))  # damage based on Attack
    currentHP = monster2.takeDamage(damage)  # enemy takes damage
    if(currentHP < 0):
        break
    print("Dein Pokemon " + monster2.name + " nahm " + str(damage) + " Punkte Schaden")
    print("______________________________________________")
    print
    time.sleep(4)

    #                                       player
    print("Player:" + monster2.trainer + "                          Tasche[0]")
    print("Pokemon: " + monster2.name + "                   current HP: " + str(monster2.life_points))
    monster2.showAttacks()
    option = input()  # choose Attack

    if(option == 0):
        print("(1)Pokebälle" + "(2)Items")
        inventaroption = input()

        if(inventaroption == 1):

            rucksack.showPokeballs()
            monster2 = rucksack.choosePokemon()
            menu = False

        elif(inventaroption == 2):
            rucksack.showItems()
            heal = rucksack.chooseItem()
            print("Für welches Pokemon")
            rucksack.showPokeballs()
            healPokemon = rucksack.choosePokemon()
            healPokemon.life_points += heal
            print (healPokemon.life_points)
            menu = False



    damage = monster2.chooseAttack(option)  # damage based on Attack

    currentHP = monster1.takeDamage(int(damage))  # enemy takes damage
    if currentHP < 0:
        break
    print(monster1.trainer + "'s Pokemon " + monster1.name + " nahm " + str(damage) + " Punkte Schaden")
    time.sleep(4)

    runde += 1
    print("Runde: " + str(runde))

print('Game finished')

"""
# Gameloop


    Duell
    -Tasche 
    --neues Pokemon
    --Heilen (gegner dran  ) 
                -go to Duell
    
    


"""