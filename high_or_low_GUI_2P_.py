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
        self.Left_Cards = [i for i in range(52)]
        self.sumple_card = 0
        self.test_card = 0
        self._1P_cleared = 0
        self._2P_cleared = 0
        self.sumple_card = self.Left_Cards[random.randint(0,51)]
        self.Left_Cards.remove(self.sumple_card)
        self.test_card = self.Left_Cards[random.randint(0,50)]
        self.Left_Cards.remove(self.test_card)
        self.mark = ["crub","heart","diamond","spead"]
        self.safe = "safe"
        self.Card_Data = [52 for i in range(52)]
        self.Card_Data[self.sumple_card] = self.sumple_card
        self.Qnumber = 1
        self.turn = "1P"
        
        

    def question(self):
        while(True):
            print(str(self.turn) + " turn!")
            print(self.mark[self.sumple_card//13] + str((self.sumple_card%13)+1))
            print("high or low or same?")
            self.answer = input()
            if self.answer == "high" or self.answer == "low" or self.answer == "same" or self.answer == "a":
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
            print("error")
        
        if self.answer == true_answer:
            self.judge = "true"
            if self.turn == "1P":
                self._1P_cleared += 1
            else:
                self._2P_cleared += 1
        else:
            self.judge = "false"
            
    def return_answer(self):
        print(self.judge)
        print("answer is " + str(self.mark[self.test_card//13] + str((self.test_card%13)+1)))
        if len(self.Left_Cards) == 1:
            print("----------------------------------------------------------")
            if self._1P_cleared > self._2P_cleared:
                print("1P " + str(self._1P_cleared) + "vs" + "2P " + str(self._2P_cleared))
                print("1P win!")
                self.safe = "out"
            elif self._1P_cleared < self._2P_cleared:
                print("1P " + str(self._1P_cleared) + "vs" + "2P " + str(self._2P_cleared))
                print("2P win!")
                self.safe = "out"
            elif self._1P_cleared == self._2P_cleared:
                print("1P " + str(self._1P_cleared) + "vs" + "2P " + str(self._2P_cleared))
                print("DRAW!")
                self.safe = "out"
        else:
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
                if self.turn == "1P":
                    self.turn = "2P"
                else:
                    self.turn = "1P"
    
hal = high_and_low()
hal.start()