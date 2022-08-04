# -*- coding:utf-8 -*-
import time


class Monster:
    # Speicher
    def __init__(self, trainer, name,life_points, attacks):  # verweise auf Klassen attribute
        self.trainer = trainer
        self.name = name
        self.life_points = life_points
        self.attacks = attacks

    # objekte [row][column]

    def showAttacks(self):

        print(" ________________________________________")
        print("|    (1)" + self.attacks[0][0] + "/" + str(self.attacks[0][1]) + "         |       (2)" +
              self.attacks[1][0] + "/" + str(self.attacks[1][1]) + "   |")
        print("__________________________________________")
        print("|    (3)" + self.attacks[2][0] + "/" + str(self.attacks[2][1]) + "         |       (4)" +
              self.attacks[3][0] + "/" + str(self.attacks[3][1]) + "    |")
        print(" ________________________________________")

    def chooseAttack(self, option):
        if option == 1:
            print(self.name + " benutzt " + self.attacks[0][0])
            return self.attacks[0][1]
        elif option == 2:
            print(self.name + " benutzt " + self.attacks[1][0])
            return self.attacks[1][1]
        elif option == 3:
            print(self.name+" benutzt " + self.attacks[2][0])
            return self.attacks[2][1]
        elif option == 4:
            print(self.name+" benutzt " + self.attacks[3][0])
            return self.attacks[3][1]
        else:
            print("Angriff konnte nicht ausgeführt werden")
            return 0


    def takeDamage(self, damage):
        self.life_points -= damage
        if self.life_points <= 0:
            time.sleep(2)
            print(self.name + " ist kampfunfähig " + self.trainer + " hat verloren")
            return
        else:
            return self.life_points






