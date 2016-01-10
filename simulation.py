#import pygame
import random



Area = [10,10]





maxfood = Area[0]*Area[1]

food = 70

growth = 0.01

class Herbivore():
    def _init_(self):
        self.alive = True
        self.ID = 1
        self.fitness = 0
        self.parent = None
        self.health = 5
        self.children = None
        self.age = 0

    def reproduce(self):
        n = 0
        for i in population:
            n += 1
        parent = self
        population.append(n)
        creature.append(n)
        creature[n] = Herbivore()
        creature[n]._init_()
        creature[n].parent = parent
        creature[n].health = 3

    def live(self):

        if self.health == 0:
            self.alive = False
        if self.alive == True:
            rand = random.randint(0,100)
            rand = float(rand)
            if self.health < 10:
                if rand/100 < food/maxfood:
                    self.health = self.health + 1
                    global food
                    food = food - 1
        if self.health > 5 and self.age > 5:
            self.reproduce()
            #self.health -= 1
            self.fitness += 1
        self.age += 1



t = 0
end = 50
foodcounter = 0
creature = []
population = []
for i in range(10):
    i = i
    creature.append(i)
    population.append(i)
for i in population:
    creature[i] = Herbivore()
    creature[i]._init_()


while t < end:
    t = t + 1
    for i in population:
        healthrand = random.randint(0,9)
        healthrand = float(healthrand)
        if healthrand == 2:
            creature[i].health = creature[i].health-1
    for i in range(1,food-1):
        if food < maxfood:
            foodrand = random.randint(0,100)
            foodrand = float(foodrand)
            if foodrand/100 < growth:
                foodcounter = foodcounter + 1
    food = food + foodcounter
    foodcounter = 0
    for i in population:
        if creature[i].alive == True:
            creature[i].live()

    print "\n\n","Generation:",t
    print "\nFood:",food,"\n"
    for i in population:
        if  creature[i].alive == True:
            print "Creature",i,"    Fitness:",creature[i].fitness,"    Health:",creature[i].health
        else:
            print "Creature",i,"    Fitness:",creature[i].fitness,"    Dead"





