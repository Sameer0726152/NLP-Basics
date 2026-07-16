from nltk.tokenize import word_tokenize
from nltk.stem.lancaster import LancasterStemmer

text = "Hello, world! This is a test sentence. Let's see how it tokenizes."

stemming = LancasterStemmer()
final_list = [stemming.stem(word) for word in word_tokenize(text)]
print(final_list)