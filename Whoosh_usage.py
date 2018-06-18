'''from whoosh.lang.porter import stem
print(stem("enhanced"))

from whoosh.lang.morph_en import variations
print(variations("enhanced"))
'''
from whoosh.fields import Schema, TEXT, KEYWORD, ID, STORED
from whoosh.analysis import StemmingAnalyzer
from whoosh.formats import Frequency
from whoosh.index import create_in
from whoosh.lang.porter import stem
from whoosh.lang.morph_en import variations

schema = Schema(title = TEXT(stored=True),
    			content = TEXT(vector=Frequency),
    			path = ID(stored=True))

ix = create_in("indexdir", schema)

myfile = open("Fs_1.txt", "r")
print(myfile)

writer = ix.writer()
writer.add_document(title=u"My the document", content=myfile.read(),
                    path=u"/a")
writer.add_document(title=u"My the document two", content=u"This is my third test document!",
                    path=u"/a")
'''writer.add_document(title=u"Second try", content=u"This is the second third example.",
              path=u"/b")
writer.add_document(title=u"Third time's the charm", content=u"Examples are third many.",
                    path=u"/c")'''
writer.commit()

from whoosh.qparser import QueryParser
with ix.searcher() as s:
	qp = QueryParser("content", schema=ix.schema)
	for i in variations("enhanced"):
		q = qp.parse(i)
	#q = stem(q)
		results = s.search(q)
		print(results)

print(variations("enhanced"))
'''from whoosh.index import create_in
from whoosh.fields import *
schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT)
ix = create_in("indexdir", schema)
writer = ix.writer()
writer.add_document(title=u"First document", path=u"/a",content=u"This is the first document we've added!")
writer.add_document(title=u"Second document", path=u"/b",content=u"The second one is even added more interesting!")
writer.commit()
from whoosh.qparser import QueryParser
with ix.searcher() as searcher:
	query = QueryParser("content", ix.schema).parse("we")
	results = searcher.search(query)
	print(results)'''