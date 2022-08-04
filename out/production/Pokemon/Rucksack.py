# -*- coding:utf-8 -*-


class Rucksack:
    def __init__(self, monster):
        self.besitzer = None
        self.Monster = monster
        self.items = [["MaxHeilung",50],
                      ["MedHeilung",25],
                      ["miniHeilung",5]]

    def InventarSystem(self):
        print("(1)Pokebälle" + "(2)Items")
        inventaroption = input()
        if(inventaroption == 1):
            self.showPokeballs()
            self.choosePokemon()
        elif(inventaroption == 2):
            self.showItems()
            self.chooseItem()


    def showPokeballs(self):
        print "Willst du ein anderes Pokemon wählen?"
        for pokemon in self.Monster:
            print pokemon.name + " " + str(pokemon.life_points)

    def choosePokemon(self):
        option = input()-1
        newPokemon = self.Monster[option]
        print "Du hast " + newPokemon.name + " gewählt"
        return newPokemon

    def showItems(self):
        for item in enumerate(self.items):
            print item

    def chooseItem(self):
                choice = input()
                choice -= 1
                item = self.items[choice][1]
                print("Willst du " + self.items[choice][0] + " benutzen? ")
                print (str(item))
                return item

    def checkifAlive(self):
        for x in self.Monster:
            return x.life_points


#rucksack = Rucksack()
#rucksack.checkifAlive()

for x in range(4):
    for y in range(3):
        print(x,y)