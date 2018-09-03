#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
author: Hunter Stabler
DESCRIPTION: python poem generator
LICENSE:GNU General Public License
created August 28th 2018
"""

import random

# "list of nouns"
nouns = ["savant", "sheeple", "weavel", "goober", "tuber", "owl", "bowels",
         "carpet", "snack", "arch", "toenail", "horse hair", "compost", "casm", 
        "pocket", "dullard", "mallard", "listicle", "miracle", "awl", 
        "Demiurge"  ]

# list of verbs
verbs = ["flies", "whacks", "dabbles", "immolates", "tastes", "summons",
         "channels", ]

# list of adjectives
adjectives = ["cold", "frumpy", "acrid", "sour", "toasty", "smarmy", "doty",
              "spidery", "wispy", "angular", "sharp", "tiniest", "basic", 
              "omnipresent", "oracular", "miraculous", "super computer", 
              "awe inspiring"]

adverbs = ["slinkily", "eagerly", "brutally", "unabashedly", "daily", "soon", 
           "outside", "underground","prophetically", "extremely"  ]
noun = random.choice(nouns)
second_noun = random.choice(nouns)
third_noun = random.choice(nouns)

verb = random.choice(verbs)
second_verb = random.choice(verbs)

adjective = random.choice(adjectives)
second_adjective = random.choice(adjectives)

adverb = random.choice(adverbs)

##concatenation
#print "The " + adjective + ", " + second_adjective + " " + noun + " " + verb

#word poem
#print "The " + adjective + " " + noun + ""
## for loop to iterate through verbs
#i = 1
#for verb in verbs:
#    whitespace = " " * i
#    print whitespace + verb
#    i = i + 1




#string formatting
print "The {adj} {n} {adv} {v} a {sn} whilst the {tn} {sv}.".format(adj=adjective,
           n=noun, v=verb, sn=second_noun, tn=third_noun, sv=second_verb, 
           adv=adverb, )

#i = 0
#for noun in nouns:
#    print nouns[i]
#    i = i + 1


