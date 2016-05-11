#import pygame
import random


# DNA implementieren


Area = [20,20]





maxfood = Area[0]*Area[1]

food = 250

growth = 0.01

class Herbivore():
    def _init_(self):
        self.alive = True
        self.note = None
        self.fitness = 0
        self.parent = None
        self.health = 5
        self.children = None
        self.age = 0
        self.DNA ={}
        self.childbirth = 0

    def reproduce(self):
        n = 0
        for i in population:
            n += 1
        parent = self
        population.append(n)
        herbi.append(n)
        herbi[n] = Herbivore()
        herbi[n]._init_()
        herbi[n].parent = parent
        herbi[n].health = 4
        self.childbirth = 1

    def live(self):

        if self.health == 0:
            self.alive = False
            if self.parent != None:
                self.parent.fitness -= 1
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
            self.health -= 4
            self.fitness += 1


        self.age += 1
        if self.childbirth == 5:
            self.childbirth = 0
        if self.childbirth > 0 and self.childbirth < 5:
            self.childbirth += 1


class Carnivore():
    def _init_(self):
        self.alive = True
        self.note = None
        self.fitness = 0
        self.parent = None
        self.health = 5
        self.children = None
        self.age = 0
        self.DNA ={}
        self.childbirth = 0
        self.huntercount = 0

    def reproduce(self):
        n = 0
        for i in population_2:
            n += 1
        parent = self
        population_2.append(n)
        carni.append(n)
        carni[n] = Carnivore()
        carni[n]._init_()
        carni[n].parent = parent
        carni[n].health = 4
        self.childbirth = 1

    def live(self):

        if self.health == 0 or self.health < 0:
            self.alive = False
            if self.parent != None:
                self.parent.fitness -= 1
        if self.alive == True:
            rand = random.randint(0,100)
            rand = float(rand)
            if self.health < 10:
                global meat
                n = 0
                for i in population:
                    n += 1
                meat = n

                if rand/100 < meat/50:
                    self.health = self.health + 1
                    randherbi = random.randint(1,meat-1)
                    if herbi[randherbi].note != "Eaten":
                        herbi[randherbi].alive = False
                        herbi[randherbi].note = "Eaten"
                        self.huntercount += 1
        if self.health > 5 and self.age > 5 and self.childbirth == 0:
            self.reproduce()
            self.health -= 4
            self.fitness += 1


        self.age += 1
        if self.childbirth == 5:
            self.childbirth = 0
        if self.childbirth > 0 and self.childbirth < 5:
            self.childbirth += 1








t = 0
end = 100
foodcounter = 0
herbi = []
population = []
carni = []
population_2 = []
for i in range(20):
    i = i
    herbi.append(i)
    population.append(i)
for i in population:
    herbi[i] = Herbivore()
    herbi[i]._init_()
for i in range(10):
    i = i
    carni.append(i)
    population_2.append(i)
for i in population_2:
    carni[i] = Carnivore()
    carni[i]._init_()


while t < end:
    t = t + 1
    for i in population:
        healthrand = random.randint(0,9)
        healthrand = float(healthrand)
        if healthrand == 2:
            herbi[i].health = herbi[i].health-1

    for i in population_2:
        healthrand = random.randint(0,9)
        healthrand = float(healthrand)
        if healthrand == 2:
            carni[i].health = carni[i].health-1
    for i in range(1,food-1):
        if food < maxfood:
            foodrand = random.randint(0,100)
            foodrand = float(foodrand)
            if foodrand/100 < growth:
                foodcounter = foodcounter + 1
    food = food + foodcounter
    foodcounter = 0
    for i in population:
        if herbi[i].alive == True:
            herbi[i].live()
    for i in population_2:
        if carni[i].alive == True:
            carni[i].live()

    print "\n\n","Generation:",t
    print "\nFood:",food,"\n"

    print "Herbivores:\n"
    for i in population:
        if  herbi[i].alive == True:
            print "Herbi",i,"    Fitness:",herbi[i].fitness,"    Health:",herbi[i].health
        else:
            if herbi[i].note == "Eaten":
                print "Herbi",i,"    Fitness:",herbi[i].fitness,"    Eaten"
            else:
                print "Herbi",i,"    Fitness:",herbi[i].fitness,"    Dead"

    print "\n\nCarnivores:\n"
    for i in population_2:
        if  herbi[i].alive == True:
            print "Carni",i,"    Fitness:",carni[i].fitness,"    Health:",carni[i].health,"    Animals hunted:",carni[i].huntercount
        else:
            print "Carni",i,"    Fitness:",carni[i].fitness,"    Dead","          Animals hunted:",carni[i].huntercount





