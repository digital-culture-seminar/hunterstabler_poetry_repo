#filename: SentenceGen.py
#author: Jake Medina

import random

nouna=[]
adja=[]
adva=[]
verba=[]
arta=[]
conja=[]
inta=[]
prepa=[]
proa=[]
ptsl=[]
queue=[]
end=False
nouncount=0
adjcount=0
advcount=0
verbcount=0
artcount=0
conjcount=0
intcount=0
prepcount=0
procount=0
nouncounto=0
adjcounto=0
advcounto=0
verbcounto=0
artcounto=0
conjcounto=0
intcounto=0
prepcounto=0
procounto=0
nouncheck='noun'
adjcheck='adjective'
advcheck='adverb'
verbcheck='verb'
artcheck='article'
conjcheck='conjunction'
intcheck='interjection'
prepcheck='preposition'
procheck='pronoun'


path=('/Volumes/JM ACE/ACE 2013-14/Programming/Python Programs/SentenceGen/')

noun=('/Volumes/JM ACE/ACE 2013-14/Programming/Python Programs/SentenceGen/noun.txt')
adj=('/Volumes/JM ACE/ACE 2013-14/Programming/Python Programs/SentenceGen/adjective.txt')
adv=('/Volumes/JM ACE/ACE 2013-14/Programming/Python Programs/SentenceGen/adverb.txt')
verb=('/Volumes/JM ACE/ACE 2013-14/Programming/Python Programs/SentenceGen/verb.txt')
art=('/Volumes/JM ACE/ACE 2013-14/Programming/Python Programs/SentenceGen/article.txt')
conj=('/Volumes/JM ACE/ACE 2013-14/Programming/Python Programs/SentenceGen/conjunction.txt')
int=('/Volumes/JM ACE/ACE 2013-14/Programming/Python Programs/SentenceGen/interjection.txt')
prep=('/Volumes/JM ACE/ACE 2013-14/Programming/Python Programs/SentenceGen/preposition.txt')
pro=('/Volumes/JM ACE/ACE 2013-14/Programming/Python Programs/SentenceGen/pronoun.txt')

infile=open(noun,'r')
infile=open(adj,'r')
infile=open(adv,'r')
infile=open(verb,'r')
infile=open(art,'r')
infile=open(conj,'r')
infile=open(int,'r')
infile=open(prep,'r')
infile=open(pro,'r')

#Read Noun
with open(noun) as f:
    for line in f:
        nouna.append(line)
# f = open(noun)
# for line in f:
#     nouna.append(f)
# f.close()

nounr=random.randint(0,len(nouna)-1)
nounc=nouna[nounr]

#Read Adjective
with open(adj) as f:
    for line in f:
        adja.append(line)

adjr=random.randint(0,len(adja)-1)
adjc=adja[adjr]

#Read Adverb
with open(adv) as f:
    for line in f:
        adva.append(line)

advr=random.randint(0,len(adva)-1)
advc=adva[advr]

#Read Verb
with open(verb) as f:
    for line in f:
        verba.append(line)

verbr=random.randint(0,len(verba)-1)
verbc=verba[verbr]

#Read Article
with open(art) as f:
    for line in f:
        arta.append(line)

artr=random.randint(0,len(arta)-1)
artc=arta[artr]

#Read conjunction
with open(conj) as f:
    for line in f:
        conja.append(line)

conjr=random.randint(0,len(conja)-1)
conjc=conja[conjr]

#Read Interjection
with open(int) as f:
    for line in f:
        inta.append(line)

intr=random.randint(0,len(inta)-1)
intc=inta[intr]

#Read Preposition
with open(prep) as f:
    for line in f:
        prepa.append(line)

prepr=random.randint(0,len(prepa)-1)
prepc=prepa[prepr]

#Read Pronoun
with open(pro) as f:
    for line in f:
        proa.append(line)

pror=random.randint(0,len(proa)-1)
proc=proa[pror]

#Pick Parts of Speech
while end == False:
  pts=raw_input('Enter each part of speech you want in the sentence in order.\nList of Parts of Speech:\nnoun\nadjective\nadverb\nverb\narticle\nconjunction\ninterjection\npreposition\npronoun\nPress Enter to confirm.\n')
  ptsl.append(pts)
  print
  if pts=='':
    end=True
    ptsl.remove('')

print ptsl

if 'noun' in ptsl:
  nouncounto=ptsl.count('noun')
  while nouncount <> 0:
    nouncount=ptsl.count('noun')
    order=ptsl.index('noun')
    queue.append(order,'noun')
    print nounc
    ptsl.remove('noun')
    nouncount=nouncount-1
  # elif isinstance('adjective',ptsl):
  #   adjcount=ptsl.count('adjective')
  # elif isinstance('adverb',ptsl):
  #   advcount=ptsl.count('adverb')
  # elif isinstance('verb',ptsl):
  #   verbcount=ptsl.count('verb')
  # elif isinstance('article',ptsl):
  #   artcount=ptsl.count('article')
  # elif isinstance('conjunction',ptsl):
  #   conjcount=ptsl.count('conjunction')
  # elif isinstance('interjection',ptsl):
  #   intcount=ptsl.count('interjection')
  # elif isinstance('preposition',ptsl):
  #   prepcount=ptsl.count('preposition')
  # elif isinstance('pronoun',ptsl):
  #   procount=ptsl.count('pronoun')

print nouncounto
print queue
# print adjcount
# print advcount
# print verbcount
# print artcount
# print conjcount
# print intcount
# print prepcount
# print procount

#print 'Noun:',nounc,'\nAdjective:',adjc,'\nAdverb:',advc,'\nVerb:',verbc,'\nArticle:',artc,'\nconjunction:',conjc,'\nInterjection:',intc,'\nPreposition:',prepc'\nPronoun:',proc
# print 'Noun:',nounc
# print 'Adjective:',adjc
# print 'Adverb:',advc
# print 'Verb:',verbc
# print 'Article:',artc
# print 'conjunction:',conjc
# print 'Interjection:',intc
# print 'Preposition:',prepc
# print 'Pronoun:',proc
infile.close()
