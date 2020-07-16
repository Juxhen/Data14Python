import nltk
from nltk.corpus import words

nltk.download()
word_list = words.words()
print (len(word_list))