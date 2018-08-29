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
nouns = ["salor", "sheeple", "weavel", "goober"]

# list of verbs
verbs = ["flies", "whacks", "dabbles", "immolates", "tastes"]

# list of adjectives
adjectives = ["cold", "frumpy", "acrid", "sour", "toasty", "smarmy"]

noun = random.choice(nouns)

verb = random.choice(verbs)

adjective = random.choice(adjectives)
second_adjective = random.choice(adjectives)

##concatenation
#print "The " + adjective + ", " + second_adjective + " " + noun + " " + verb

#word poem
print "The " + adjective + " " + noun + ""
# for loop to iterate through verbs
i = 1
for verb in verbs:
    whitespace = " " * i
    print whitespace + verb
    i = i + 1
#string formatting
#print "The {adj} {n} {v}.".format(adj=adjective, n=noun, v=verb)

#i = 0
#for noun in nouns:
#    print nouns[i]
#    i = i + 1


