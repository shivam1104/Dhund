import spacy

from spacy.lang import en


nlp = spacy.load("en")

myfile = open("Fs_2.txt", "r")
document = myfile.read()
document = document.lower()
document_stem = document

import gensim
from gensim import parsing
document_stem = gensim.parsing.stem_text(document_stem)


document = nlp(document)
document_stem = nlp(document_stem)
'''
print(dir(document))
print(document[0])
print(list(document.sents))

all_tags = {w.pos: w.pos_ for w in document}
print(all_tags)

for word in list(document.sents)[2]:  
    print(word, word.tag_)
'''
print("document_stem"+str(document_stem))
contract = [sent for sent in document.sents if 'contract' in sent.string.lower()]
contract_stem = [sent for sent in document_stem.sents if 'contract' in sent.string.lower()]

print("Without Stemming")
for sente in contract:
	#sentence = hotel[0] 
	for word in sente:
		print(word, ': ', str(list(word.children)))




print("With Stemming")
print(contract_stem)
for stem_sent in contract_stem:
	for word in stem_sent:
		print(word, ': ', str(list(word.children)))








'''import hunspell
hobj = hunspell.HunSpell('/usr/share/myspell/en_US.dic', '/usr/share/myspell/en_US.aff')
hobj.spell('spookie')'''