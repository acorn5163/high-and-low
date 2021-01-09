# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 15:30:57 2020
@author: keigo
"""

import numpy as np
import random

class LifeGame():
    def __init__(self):
        self.size = 10
        self.life = 50
        self.field = np.zeros((self.size,self.size), dtype = str)
        self.fieldB = np.zeros((self.size,self.size), dtype = str)
        self.length = 0
        self.width = 0
        self.counter = 0
        self.type = 0
        
    
    def fieldmaker(self):
        for i in range(self.size):
            for j in range(self.size):
                self.field[i,j] = '◯'
        for i in range(self.life):
            self.field[random.randint(0,self.size-1),random.randint(0,self.size-1)] = '●'
        self.fieldB = self.field
    
        self.fieldB = self.field
    def printfield(self):
        print(self.field)
        print("------------------")
    
    def checker(self):
        if self.length == 0 and self.width == 0:
            self.type = 7
        elif self.length == 0 and self.width == self.size-1:
            self.type = 5
        elif self.length == self.size-1 and self.width == 0:
            self.type = 8
        elif self.length == self.size-1 and self.width == self.size-1:
            self.type = 6
        elif self.length == 0 and self.width != 0 and self.width != self.size-1:
            self.type = 1
        elif self.length == self.size-1 and self.width != 0 and self.width != self.size-1:
            self.type = 2
        elif self.width == self.size-1 and self.length != 0 and self.length != self.size-1:
            self.type = 3
        elif self.width == 0 and self.length != 0 and self.length != self.size-1:
            self.type = 4
        else:
            self.type = 0

    
    def Counter(self):
        self.counter = 0
        if self.type == 0:
            if self.field[self.length+1,self.width] == '●':
                self.counter += 1
            if self.field[self.length-1,self.width] == '●':
                self.counter += 1
            if self.field[self.length,self.width+1] == '●':
                self.counter += 1
            if self.field[self.length,self.width-1] == '●':
                self.counter += 1
            
        if self.type == 1:
            if self.field[self.length+1,self.width] == '●':
                self.counter += 1
            if self.field[self.length,self.width-1] == '●':
                self.counter += 1
            if self.field[self.length,self.width+1] == '●':
                self.counter += 1
        if self.type == 2:
            if self.field[self.length-1,self.width] == '●':
                self.counter += 1
            if self.field[self.length,self.width-1] == '●':
                self.counter += 1
            if self.field[self.length,self.width+1] == '●':
                self.counter += 1
        if self.type == 3:
            if self.field[self.length,self.width-1] == '●':
                self.counter += 1
            if self.field[self.length+1,self.width] == '●':
                self.counter += 1
            if self.field[self.length-1,self.width] == '●':
                self.counter += 1
        if self.type == 4:
            if self.field[self.length,self.width+1] == '●':
                self.counter += 1
            if self.field[self.length+1,self.width] == '●':
                self.counter += 1
            if self.field[self.length-1,self.width] == '●':
                self.counter += 1
        if self.type == 5:
            if self.field[self.length,self.width-1] == '●':
                self.counter += 1
            if self.field[self.length+1,self.width] == '●':
                self.counter += 1
        if self.type == 6:
            if self.field[self.length-1,self.width] == '●':
                self.counter += 1
            if self.field[self.length,self.width-1] == '●':
                self.counter += 1
        if self.type == 7:
            if self.field[self.length+1,self.width] == '●':
                self.counter += 1
            if self.field[self.length,self.width+1] == '●':
                self.counter += 1
        if self.type == 8:
            if self.field[self.length-1,self.width] == '●':
                self.counter += 1
            if self.field[self.length,self.width+1] == '●':
                self.counter += 1
    
    def judger(self):
        if self.field[self.length,self.width] == '●':
            if self.counter == 0 or self.counter == 1 or self.counter == 4:
                self.fieldB[self.length,self.width] = '●' 
            else:
                self.fieldB[self.length,self.width] = '◯'
        
        if self.field[self.length,self.width] == '◯':
            if self.counter == 3:
              self.fieldB[self.length,self.width] = '●' 
            else:
                self.fieldB[self.length,self.width] = '◯'

    def mainsystem(self):
        self.fieldmaker()
        for i in range(10):
            self.printfield()
            for self.length in range(self.size):
                for self.width in range(self.size):
                    self.checker()
                    self.Counter()
                    self.judger()
                    self.field = self.fieldB


lifegame = LifeGame()
lifegame.mainsystem()