# -*- coding: utf-8 -*-
"""
@author: Rizaraf
"""

import os

def getVocabList():
    """
    GETVOCABLIST reads the fixed vocabulary list in vocab.txt and returns a
    cell array of the words
    vocabList = GETVOCABLIST() reads the fixed vocabulary list in vocab.txt 
    and returns a cell array of the words in vocabList.
    """

    path = os.path.join(os.getcwd(),"dataSets")
    
    vocabList = []
    i=0
    with open(os.path.join(path,"vocab.txt"),'r') as f:
        for line in f:
            for word in line.split():
                if i%2 == 1:
                    vocabList.append(word)
                i+=1
    
    return vocabList
