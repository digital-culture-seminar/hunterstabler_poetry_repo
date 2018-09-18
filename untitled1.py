#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 20:08:21 2018

@author: hunterstabler
"""
#white space
#line breaks
# "flow control binches!!!!!xxx"

import random

names = ["Abdul", "Yianni", "Kam", "Dunderblizten", "Willow"]

pronouns = ["he", "she", "it"]

random.seed()

name = random.choice(names)
pronoun = random.choice(pronouns)



print "On a wet night, {name} ate a pile of ashes.\
 {pronoun} drenk blech. {name} then rolled the dice.\
 ".format(name=name, pronoun=pronoun.capitalize())
 
roll = random.randint(1,6)
print "{Name} rolled a {roll}".format(Name=name, roll=roll)

if roll == 1:
    print "Bad luck, sour master!"
elif roll == 6:
    print "Glory unto you, power up!!!"
    
else:
    print "CHampion is happy and dead!"
    

    