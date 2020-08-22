# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 00:39:52 2020

@author: keigo
"""

import matplotlib.pyplot as plt
from PIL import Image,ImageOps
import numpy as np
import random
import os



class high_and_low:
    def __init__(self):
        self.Cleared_cards = []
        self.Left_Cards = [i for i in range(52)]
        self.sumple_card = 0
        self.test_card = 0
        self.cleared = 0
        self.left_wrong = 15
        self.sumple_card = self.Left_Cards[random.randint(0,51)]
        self.Left_Cards.remove(self.sumple_card)
        self.test_card = self.Left_Cards[random.randint(0,50)]
        self.Left_Cards.remove(self.test_card)
        self.mark = ["crub","heart","diamond","spead"]
        self.safe = "safe"
        self.Card_Data = [52 for i in range(52)]
        self.Card_Data[self.sumple_card] = self.sumple_card
        self.Qnumber = 1
        
        

    def question(self):
        while(True):
            print(self.mark[self.sumple_card//13] + str((self.sumple_card%13)+1))
            print("high or low or same?")
            self.answer = input()
            if self.answer == "high" or self.answer == "low" or self.answer == "same" or self.answer == "test":
                break
            else:
                print("please write high or low or same")
        
            
    def picturesystem(self):
        fig=plt.figure(figsize=(13, 6),facecolor = "navy")
        columns = 13
        rows = 4
        for i in range(52):
                imgname =r"C:\Users\keigo\program\trumppictures" + "\\" + str(self.Card_Data[i]) + ".png"
                im = Image.open(imgname).convert('RGB')
                im_list = np.asarray(im)
                fig.add_subplot(rows, columns, i+1)
                plt.axis("off")
                plt.imshow(im_list)
        plt.show()
    
    def judge_answer(self):
        if self.sumple_card%13 > self.test_card%13:
            true_answer = "low"
        elif self.sumple_card%13 < self.test_card%13:
            true_answer = "high"
        elif self.sumple_card%13 == self.test_card%13:
            true_answer = " same"
        else:
            print(error)
        
        if self.answer == true_answer:
            self.judge = "true"
            self.Cleared_cards.append(str(self.sumple_card))
            self.cleared += 1
        else:
            self.judge = "false"
            self.left_wrong -= 1
            if self.left_wrong <= 0:
                self.safe = "out"
            else:
                self.safe = "safe"
            
    def return_answer(self):
        print(self.judge)
        print("answer is " + str(self.mark[self.test_card//13] + str((self.test_card%13)+1)))
        if self.safe == "out":
            print("gameover! Your score is " + str((self.cleared)) + "/52")
            
        elif len(self.Left_Cards) == 1:
            print("Game Clear!")
            self.safe = "out"
        else:
            print("left Chance is " + str(self.left_wrong))
            print("Next question!")
            print("----------------------------------------------------------")
    def start(self):
        while(True):
            self.picturesystem()
            self.question()
            self.judge_answer()
            self.return_answer()
            if self.safe == "out":
                self.Card_Data = [i for i in range(52)]
                self.picturesystem()
                break
            else:
                self.sumple_card = self.test_card
                self.test_card = self.Left_Cards[random.randint(0,(len(self.Left_Cards)-1))]
                self.Left_Cards.remove(self.test_card)
                print(str(self.Qnumber) + " | "+ str(len(self.Left_Cards)))
                self.Qnumber += 1
                print(len(self.Left_Cards))
                self.Card_Data[self.sumple_card] = self.sumple_card
    
hal = high_and_low()
hal.start()