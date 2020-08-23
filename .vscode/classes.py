import numpy as np
import random as rd
import time

class activeWord:
    def __init__(self, word, lane, dragLength): # po co ten self w init? Napisane nizej
        self.text = word
        self.lane = lane    # self = this
        self.drag = dragLength
    
    def __init__(self, text, lane):             # default drag = 0
        self.text = text
        self.lane = lane    # self = this
        self.drag = 0

# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class. It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:

class road:
    def __init__(self):
        self.isAvailable = True
        self.cooldown = 0
        self.lastWordLen = 20

    def tick(self):
        self.cooldown -= 1

        if (self.cooldown == 0):
            self.isAvailable = True

    def setCooldown(self, word):
        self.cooldown = len(word)
        self.lastWordLen = len(word)

class roads:
    def __init__(self, rows):
        self.roadBoard = []
        for x in range(rows):
            self.roadBoard.append(road())
            

    def tickAll(self):
        for r in self.roadBoard:
            r.tick()

    def printRoads(self):
        for r in self.roadBoard:
            print('a: ' + str(r.isAvailable) + ' | cd: ' + str(r.cooldown))
        print('\n')
        return

    def pickEmptyRoad(self, text):
        tmp = self.roadBoard.copy()
        indices = list( range( len( tmp ) ) )

        while(len(indices) > 0):
            rnd = rd.choice(indices)

            if (tmp[rnd].isAvailable == True and len(text) < tmp[rnd].lastWordLen - tmp[rnd].cooldown):
                self.roadBoard[rnd].isAvailable = False
                return rnd
            
            else:
                indices.remove(rnd)

        return -1



