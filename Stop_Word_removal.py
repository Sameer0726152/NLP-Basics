from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import nltk
from string import punctuation

text = "Hello, world! This is a test sentence. Let's see how it tokenizes."

#Making list of stop words and punctuation to remove from the text

custom_list = set(stopwords.words('english') + list(punctuation))
word_list = [word for word in word_tokenize(text) if word not in custom_list]
print("Words after stop word removal:", word_list)