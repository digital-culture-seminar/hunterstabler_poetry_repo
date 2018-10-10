#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 11:35:45 2018

@author: hunterstabler
"""

#new word poem with multiple corpus sources

import random


with open ("adjective.txt") as file:
    adj = file.read()
    
with open ("adverb.txt") as file:
    adv = file.read()
    
with open ("article.txt") as file:
    art = file.read()
    
with open ("conjunction.txt") as file:
    conj = file.read()
    
with open ("interjection.txt") as file:
    intj = file.read()
    
with open ("noun.txt") as file:
    nn = file.read()
    
with open ("preposition.txt") as file:
    prep = file.read()
    
with open ("pronoun.txt") as file:
    pron = file.read()
    
with open ("verb.txt") as file:
    vrb = file.read()
    mylist = []
    line = next(vrb)
    mylist.append(line)

print mylist

    
n = random.choice(nn)
v = random.choice(vrb)


print v

#add precip = csv.reader(csv)
#look up csv reader and import csv