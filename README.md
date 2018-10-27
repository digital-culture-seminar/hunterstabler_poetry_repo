
# Hunter Stabler
## Poet/Artist Statement
### Digital Culture Seminar

I am using a Markov Generator to create a poem that uses many Keats' poems and one of my poems as the source of text. I will experiment with weighting the libraries to get desirable results that reflect the style of both poets. Currently the flavor favors Keats because there is just so much more Keats material that the generator is sourcing from.

I aim to use code as a divination tool to access the collective consciousness of computational chance at a continually changing present moment. My curation of the results is dictated by the throwing of sticks. The creation and curation of my poetry corpus is channeled from the trance state induced through the virtual chewing of the leaves of the Salvia Divinorum plant-teacher and her accompanying light body as she transects linear time, within a modded version of the video game *The Sims4*. Through the simulated avatar-shaman’s piecemeal quantum scanning of linear causality within the video game, we hope to coax a  multidimensional cymatic hologram of the virtual eschaton, which will theoretically be analogous to the hyperdimensional object at the end of time within the “real” universe as well. Thus, by glimpsing a crude digital sketch of the eschatological eye of the ineffable,  I can better prepare for uploading my existence into non-linear communion with the bold axis of cosmological infinite programmatic knowledge when my mortal coil becomes obsolete.

Two Markov generator augmented poem examples can be seen below. The first has equal weighting between the text samples and the second is weighted 40 to 1 in favor of my poem, the second is weighted 40 to 1 from my poetry to Keats:

## A Testuary Exegesis
```
Only you have the goodliest view of this sweet spot, Some fainter gleamings o'er his book: 
Who had power to make me sick of joy and pain; 
Clasp'd like a milk-white lamb that bleats for man's protection.
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
Gentle windings to the tender greening of April meddles.
```


```
This passion lifted upon his arm he lean'd; not rising, from supreme contempt.
```


```
Silent entangler of a leafy world 
we rest in hope to see 
no other breezes than are blown through verdurous glooms and winding mossy ways.
```


```
Let the mad poets say whate'er they please of the leaves hast never told 
how, from a land of fragrance, quietness, and trees, and flowers mold.
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
that each had found a little noiseless noise among the em'rald tresses; 
While the ermine let music wander skittering round my ears.
```


## Songs of mine
```
What is more soothing to me than these songs of mine?
```
```
Who shall his fame impair when thou art capable,
As thou exceedest all things in thy silent mind?
Unbounded knowledge makes a God as wrathful as himself.
Thou hath smelteth surely dealteth
unholy effervescent vespers of the swine
```
```
Redolent of sulfur twine
round esters offside apothecary shelf
tremors imbibe
a crescent indigo swill
```
```
calming ghostly pipes
monotrope amethyst sleep;
orbs blink and soften
Esper's crystal eye.
```
```
A pauper's coffin
from billowy vagueness shies
```
```
Unravish'd bride of quietness,
Thou foster-child of silence
and slowly animated through clouds of divinorum
and of morn float in voluptuous fleeces o'er the quartz clearness,
to woo its own sad image into nearness:
Death to light you, or mourn the light of death to show you,
beryl fissure leaks like thin silver streaks across the sky,
And I will tell thee what thou wouldst have been?
```
```
Nay, a blackest shape
reconciled internally
```
```
horselike tourmaline
```
```
Knowing now each piece
```
```
Not waiting until after to learn what it has to teach
```
```
For what a height my spirit leaps, and prances,
E'en then my soul with exultation dances
for that finality from outside perspective glances.
```
```
Shut up senses, telesthesiastic gyres
wait in the stillness.
Finally from inside perspective smote
reckoning prescient illness
```
```
a rattling that unhinged the mind from time
```
```
What bezel lens through the bee-mouth sips:
Ay, in those meads where sometimes secrets to the puzzle finds
```
```
endgame buzzer ringing tines
```
```
echoes in a compound eye
```
```
O let me taste that sweet sound once more,
the thought after thought to nourish uphill gyroscopic spires
trickle down from cathedral vaulting antipodal pole of the hivemind
```
```
involuntarily
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

synthesized_model = markovify.combine([power_model, bull_model, pag_model],[10,1,1])

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
    
    
with open("keats_poem_10.md", "a") as f:
    f.write("""

```
{poem}
```
""".format(poem=poem))
