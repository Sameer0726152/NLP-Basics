from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.collocations import BigramCollocationFinder

text = "Hello, world! This is a test sentence. Let's see how it tokenizes."
Stopword_list = set(stopwords.words('english') + list(punctuation))
Final_list = [word for word in word_tokenize(text) if word not in Stopword_list]
print(Final_list)

Bigram_List = BigramCollocationFinder.from_words(Final_list)
print(Bigram_List.ngram_fd.items())