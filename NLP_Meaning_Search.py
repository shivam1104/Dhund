from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from pandas import Series
import nltk
from nltk.corpus import wordnet

def tag(x):
    return pos_tag(word_tokenize(x))



synonyms = []
antonyms = []
 
for syn in wordnet.synsets("document"):
	#print("Down2")
	print (syn)
	#print("Down")
	for l in syn.lemmas():
		print(" \n")
		print(l)
		synonyms.append(l.name())
		if l.antonyms():
			antonyms.append(l.antonyms()[0].name())
 
print(set(synonyms))
print(set(antonyms))

for i in synonyms:
	print(tag(i))

print(tag(""))
