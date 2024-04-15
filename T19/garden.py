import spacy 
from spacy import displacy

gardenpathSentences = ['The complex houses married and single soldiers and their families.', 'The horse raced past the barn fell.',
                       'Mary gave the child Band-Aid.', 'That Jill is never here hurts.', 'The cotton clothing is made of grows in Mississippi'] 

# Load the english language model
nlp = spacy.load("en_core_web_sm")

# Process the doc
for sentence in gardenpathSentences:
    doc = nlp(sentence)

# Tokenise sentences in list
#    for token in doc:
#      print(token.text)

# POS tagging all tokens
    for token in doc:
        print(f"{token.text:{12}} {token.pos_:{6}} {token.dep_}")  

# Named entity recognision
for sentence in gardenpathSentences:
    doc = nlp(sentence)
    print([(i, i.label_, i.label) for i in doc.ents])
  

# Explain entity
print(spacy.explain("GPE"))

print(spacy.explain("PERSON"))


# Answer to questions
# 1. 
# What is the entity and explaination you looked up?
''' Entity "GPE" is the entity which categories all countries, cities, states from the sentence. 
Specifically geopolitical entities, e.g. everything with a governing body like cities and countries. Examples: "Germany", "Buenos Aires".'''

# Did the entity make sense in terms of word associated with it?
''' Yes it does make sense for this particular sentence because 'Mississippi is name of city which sentence referring to'''


# 2.  
# What is the entity and explaination you looked up?
''' The next etity I had looked for is 'PERSON'. It categories the name of person 
'''
# Did the entity make sense in terms of word associated with it?
''' Yes. as in both sentences in the list where the words are categoried as 'PERSON' entity are names of the person 
'Jill' and 'Mary' correctly implies name meaningfully '''