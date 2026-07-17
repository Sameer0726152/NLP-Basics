from sklearn.feature_extraction.text import TfidfVectorizer
sentences = [
    "Hello, world! This is a test sentence.",
    "Let's see how it tokenizes.",
    "This is another sentence for testing.",
    "NLP is fun and interesting!"
    ]

vec = TfidfVectorizer()
vec.fit(sentences)
print(vec.vocabulary_)
print(vec.idf_)