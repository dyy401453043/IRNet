import nltk
from nltk import data
data.path.append(r'D:\NL2SQL\nltk_data')

#from nltk.book import *


tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')