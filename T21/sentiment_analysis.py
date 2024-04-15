import pandas as pd
import numpy as np
import spacy 
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import defaultdict
import seaborn as sns

# Load EN language model

nlp = spacy.load('en_core_web_sm')

# Read data file into dataframe

df = pd.read_csv('Amazon_product_reviews.csv')
df.head()
df.info()

# Select reviews.text column from dataset for analysis
reviews_data = df[['reviews.text']].dropna()
reviews_data.info()
reviews_data.head()
#clean_data = df.dropna(subset = ['reviews.text'])
#clean_data.isnull().sum()
#clean_data.info()


# Preprocessing for data

def preprocess(text):
    doc = nlp(text)
    return ' '.join([token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct])

# Function to convert preprocessed text to a SpaCy doc (which inherently contains a vector)
def get_doc(text):
    return nlp(text)
    
# Only use a small subset of the data
reviews_data = reviews_data.sample(5000, random_state = 42)

reviews_data['processed_text'] = reviews_data['reviews.text'].apply(preprocess)
reviews_data['doc'] = reviews_data['processed_text'].apply(get_doc)
  
reviews_data.head()

# Function to analyse polarity score of reviews
def analyse_polarity(text):
    
    # Analyze sentiment with TextBlob
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    
    return polarity


# Function to get sentiment 

def polarity_score(polarity):
    if polarity > 0:
        sentiment = 'positive'
    elif polarity < 0:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'
    
    return sentiment

def polarity_strength(polarity):
    if polarity == 1:
        strength = 'Very Positive'
    elif (polarity > 0 and polarity < 1):
        strength = 'Positive'
    elif polarity == 0:
        strength = 'Neutral'
    elif ( polarity < 0 and polarity > -1 ):
        strength = 'Negative'
    elif polarity == -1:
        strength = 'Very Negative'    
    return strength

# Get the polarity score, Sentiment(positive, negative and neutral) and polarity strength on review in separate columns

reviews_data['polarity_score'] = reviews_data['processed_text'].apply(analyse_polarity)

reviews_data['sentiment'] = reviews_data['polarity_score'].apply(polarity_score)

reviews_data['strength'] = reviews_data['polarity_score'].apply(polarity_strength)

reviews_data.head(20)


# Find the similarity between 2 reviews
# randomly selecting rows 5 and 10
similarity = reviews_data['doc'][5].similarity(reviews_data['doc'][10])
print(f"Cosine Similarity: {similarity}")

# Visualise polarity and sentiment analysis

# Initialize dictionaries to hold positive and negative words
positive_words = defaultdict(int)
negative_words = defaultdict(int)
for sentence in reviews_data['processed_text']:
    words = sentence.split()

    for word in words:
        blob = TextBlob(word)
        polarity = blob.sentiment.polarity

        if polarity > 0:
            positive_words[word.lower()] += 1
        elif polarity < 0:
            negative_words[word.lower()] += 1

pos_wordcloud = WordCloud(width=400, height=200, background_color ='white').generate_from_frequencies(positive_words)
neg_wordcloud = WordCloud(width=400, height=200, background_color ='white').generate_from_frequencies(negative_words)

fig, ax = plt.subplots(1, 2, figsize=(10, 5))

ax[0].imshow(pos_wordcloud, interpolation='bilinear')
ax[0].set_title('Positive Words')
ax[0].axis('off')

ax[1].imshow(neg_wordcloud, interpolation='bilinear')
ax[1].set_title('Negative Words')
ax[1].axis('off')

plt.show()

# Pie chart plot for sentiment analysis
labels = ['POSITIVE', 'NEGATIVE', 'NEUTRAL']
#colors = ['G', 'R', 'B']
plt.pie(reviews_data['sentiment'].value_counts(), autopct='%0.2f%%',colors=sns.color_palette('Set2'))

plt.title('Distribution of sentiment', size=14, y=-0.01)
plt.legend(labels, ncol=17, loc=9)
plt.show()

