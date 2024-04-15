
import spacy
from spacy import displacy


nlp = spacy.load('en_core_web_sm')

text = "Apple is looking at buy U.K. startup for $1 billion in 2021. Apples trees are awesome"
doc = nlp(text)

for token in doc:
#  print(token.text)
  print(f"{token.text:{12}}{token.pos_:{16}}{token.dep_}")

'''  
doc1 = nlp("I like salty fries and hamburgers")
doc2 = nlp("Fast food taste really good.")

similarity = doc1.similarity(doc2)
print(f"Document similarity: {similarity:.2f}")

'''


#### Named Entity Recognition (NER)
for ent in doc.ents:
  print(f"{ent.text:{16}}{ent.label_}")

