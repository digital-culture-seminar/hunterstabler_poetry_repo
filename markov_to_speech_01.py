#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 19:07:06 2018

@author: hunterstabler
"""

"""
SCRIPT:  markovify-to-speech.py
AUTHOR:  Brendan Harmon <brendan.harmon@gmail.com>
PURPOSE: Open educational materials for a seminar on digital culture
LICENSE: GNU General Public License v2
DEPENDENCIES: markovify, playsound, and gTTs
"""

# import libraries
from playsound import playsound
from gtts import gTTS
import markovify

# get raw text as string

with open ("experimental artist statement_2017.txt") as file:
    eas = file.read()
    
with open ("keats_02_edited.txt") as file:
    keats2 = file.read()
    
with open ("keats_edited.txt") as file:
    keats = file.read()
    
with open ("palace_of_pleasure.txt") as file:
    p_o_p = file.read()
    
power_model = markovify.Text(eas)
bull_model = markovify.Text(keats2)
pag_model = markovify.Text(keats)
pal_model = markovify.Text(p_o_p)

synthesized_model = markovify.combine([power_model, bull_model, pag_model],[1,1,1])

#for i in range(3):
   # print power_model.make_sentence()
    #print " "

    
poem = synthesized_model.make_sentence() + synthesized_model.make_sentence()

#with open("poem_experiment_class.md", "w") as f: 
#    f.write("## Title")
#    f.write("\n")        
#    f.write("'''")
#    f.write("\n") 
#    f.write(poem)
#    f.write("\n") 
#    f.write("'''")
    
    
with open("class_keats_poem_16.md", "a") as f:
    f.write("""

```
{poem}
```
""".format(poem=poem))

# build the markov model
text_model = markovify.NewlineText(text)

# print a randomly-generated sentence of no more than 140 characters
markov_poem = text_model.make_short_sentence(140) + text_model.make_short_sentence(140)

# text to speech
tts = gTTS(text=markov_poem, lang='en')

# write audio file
tts.save("markovified_Keats_poem_05.mp3")

# play audio file
playsound("markovified_Keats_poem_05.mp3")


