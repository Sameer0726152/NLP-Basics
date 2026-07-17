import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

sentences = [
    "Hello, world! This is a test sentence.",
    "Let's see how it tokenizes.",
    "This is another sentence for testing.",
    "NLP is fun and interesting!"
    ]

dataframe = pd.DataFrame(sentences, columns=['Text'])
print(dataframe)

count_vectorizer = CountVectorizer()
idk = count_vectorizer.fit_transform(dataframe.Text).toarray()
print(idk)
print(count_vectorizer.get_feature_names_out())

count_vectorizer = CountVectorizer(stop_words = ['the', 'is'])
idk2 = count_vectorizer.fit_transform(dataframe.Text).toarray()
print(idk2)
print(count_vectorizer.vocabulary_)