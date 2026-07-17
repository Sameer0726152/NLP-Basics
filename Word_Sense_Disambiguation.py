from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.wsd import lesk

word1 = lesk(word_tokenize("Sing in a lower tone, along with the bass"), "bass")
print(word1, word1.definition())

word2 = lesk(word_tokenize("The sea bass really very hard to catch"), "bass")
print(word2, word2.definition())

word3 = lesk(word_tokenize("My mouse is not working"), "mouse")
print(word3, word3.definition())