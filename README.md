
# Digital Culture Poet
## Artist Statement

I am using a Markov Generator to create a poem that uses many Keats' poems and one of my poems as the source of text. I will experiment with weighting the libraries to get desirable results that reflect the style of both poets. Currently the flavor favors Keats because there is just so much more Keats material that the generator is sourcing from.

non working model for other idea:
I would like to create a poem generator that randomly inserts elements into a multi-sentence composed poem. The generator would add nouns, pronouns, interjections, verbs, adverbs, adjectives, and prepositions from libraries of these forms of speech that I have curated. I would like to maintain control over the composition and tone of the poem by dictating its structure and dictating the words that are present in the libraries. The elements that are left to programmatic chance and random associative meaning within the poem
will be controlled by random number generation that decides which particular nouns, verbs, adjectives, etc get paired together within the composed poem sentences and lines.


I aim to use code as a divination tool to access the collective consciousness of computational chance at a continually changing present moment. My curation of the results is dictated by the throwing of sticks. The creation and curation of my poetry corpus is channeled from the trance state induced through the virtual chewing of the leaves of the Salvia Divinorum plant-teacher and her accompanying light body as she transects linear time, within a modded version of the video game *The Sims4*. Through the simulated avatar-shaman’s piecemeal quantum scanning of linear causality within the video game, we hope to coax a  multidimensional cymatic hologram of the virtual eschaton, which will theoretically be analogous to the hyperdimensional object at the end of time within the “real” universe as well. Thus, by glimpsing a crude digital sketch of the eschatological eye of the ineffable,  I can better prepare for uploading my existence into non-linear communion with the bold axis of cosmological infinite programmatic knowledge when my mortal coil becomes obsolete.

A generated poem example can be seen below:

## A Testuary Exegesis
```
Only you have the goodliest view of this sweet spot, Some fainter gleamings o'er his book: 
Who had power to make me sick of joy and pain; 
Clasp'd like a milk-white lamb that bleats For man's protection.
```

```
What does he murmur with his maid, And to his eyes; And from the far-foamed sands.
```


```
Then in a bed of snow.
```


```
But what is fair?
```


```
The bowery shore went off in gentle windings to the tender greening of April meddles?
```


```
This passion lifted him upon his arm he lean'd; not rising, from supreme contempt.
```


```
Silent entangler of a leafy world 
we rest in hope to see 
no other breezes than are blown through verdurous glooms and winding mossy ways.
```


```
Let the mad poets say whate'er they please of the leaves hast never told 
how, from a land Of fragrance, quietness, and trees, and flowers mold.
```


```
Then, once again, the charmed God began an oath, 
and through the water round that bend; 
Not the minutest whisper does it send 
To the wide-spreaded night above her towers end.
```


```
At a touch sweet pleasure melteth like bubbles when rain pelteth; 
Then let winged fancy wander through the thought of every guest
that each, as he had found a little noiseless noise among the em'rald tresses; 
While the ermine let music wander skittering round my ears.
```

Through the intervention of many random ecstatic computational poem iterations, cryptically prophetic metaphorical meaning will spill from the shadow of the future into the present. Unfortunately, the meaning of said poems will only become fully clear to the consensus public after the events have occurred, not earlier when the prescient poem was generated. This outstanding problem of interpreting vague metaphors about future events is one best left to poets, the time tested masters of singular, direct, and objective, semiotics and semantics.

''' python

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 19:22:14 2018

@author: hunterstabler
"""
#mylist = [] i
#for i in range(0,5):
#    my_list.append(synthesized_model.make_sentence(140))

import markovify

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


poem = synthesized_model.make_sentence()

#with open("poem_experiment_class.md", "w") as f:
#    f.write("## Title")
#    f.write("\n")        
#    f.write("'''")
#    f.write("\n")
#    f.write(poem)
#    f.write("\n")
#    f.write("'''")


with open("keats_experiment_03.md", "a") as f:
    f.write("""

```
{poem}
```
""".format(poem=poem))

"""
author: Hunter Stabler
DESCRIPTION: python poem generator
LICENSE:GNU General Public License
created August 28th 2018
"""

import random


# "list of exclamations"
exclamations = ["Wow", "Yeet", "Goodbye", "Hallelujah", "Nam Myoho Renge Kyo",
                "He gave us some yogurt", "Kamehame ha", "Oh dear", "Yes",
                "Ow", "Sup bibble", "Yip", "Okay", "Hola", "And so it will be",
                "Hark"]

# "list of nouns"
nouns = ["savant", "sheeple", "weavel", "goober", "tuber", "owl", "bowels",
         "carpet", "snack", "arch", "toenail", "horse hair", "compost", "casm",
        "pocket", "dullard", "mallard", "listicle", "miracle", "awl",
        "Demiurge", "mangosteen", "Timor", "pow wow", "detour","ShamWow"]

# "list of place nouns"
place_nouns = ["hind quarters", "AA meeting", "parking lot", "noise festival",
               "Apalachians", "Zeta Reticuli", "ocean floor", "HoJo", "Dojo",
               "onsen"]

# "list of verbs"
verbs = ["hover", "whack", "dabble", "immolate", "taste", "summon",
         "channel", "throw", ]

# "list of adjectives"
adjectives = ["cold", "frumpy", "acrid", "sour", "toasty", "smarmy", "doty",
              "spidery", "wispy", "angular", "sharp", "tiniest", "basic",
              "omnipresent", "oracular", "miraculous", "super computer",
              "awe inspiring", "analogue", "analogous", "teleological"]
# "list of adverbs"
adverbs = ["slinkily", "eagerly", "brutally", "unabashedly", "daily", "soon",
           "outside", "underground","prophetically", "extremely",
           "sardonically",   ]

noun = random.choice(nouns)
second_noun = random.choice(nouns)
third_noun = random.choice(nouns)
fourth_noun = random.choice(nouns)
fifth_noun = random.choice(nouns)

verb = random.choice(verbs)
second_verb = random.choice(verbs)
third_verb = random.choice(verbs)

adjective = random.choice(adjectives)
second_adjective = random.choice(adjectives)

adverb = random.choice(adverbs)
second_adverb = random.choice(adverbs)

exclamation = random.choice(exclamations)

place_noun = random.choice(place_nouns)

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
print " {ex}, The {adj} {n} {adv} {v}s a {sn} whilst the {tn} {sv}s a {fthn}.\
 How can a {sa} {fn} {tv} in the {pn}?".format(adj=adjective,
        n=noun, v=verb, sn=second_noun, tn=third_noun, sv=second_verb,
        adv=adverb, ex=exclamation, pn=place_noun, sa=second_adjective,
        fn=fourth_noun, fthn=fifth_noun, tv=third_verb)





#i = 0
#for noun in nouns:
#    print nouns[i]
#    i = i + 1

#" How can a {sa} {fn} {tv} in the {pn}? "
