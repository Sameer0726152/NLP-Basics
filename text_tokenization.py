from nltk.tokenize import word_tokenize, sent_tokenize

text = "Hello, world! This is a test sentence. Let's see how it tokenizes."

#Tokenize the text into sentences and words

sentence = sent_tokenize(text)
print("Sentences:", sentence)
Words = word_tokenize(text)
print("Words:", Words)

#List words of sentence

word = [word_tokenize(sent) for sent in sentence]
print(word)