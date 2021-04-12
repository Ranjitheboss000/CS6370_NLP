from util import *

# Add your import statements here
from nltk.tokenize import TreebankWordTokenizer

class Tokenization():

    def naive(self, text):
        tokenizedText = [i.split() for i in text]
        return tokenizedText

    def pennTreeBank(self, text):
        tokenizedText = [TreebankWordTokenizer().tokenize(i) for i in text]
        return tokenizedText