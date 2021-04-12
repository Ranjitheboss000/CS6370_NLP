from util import *

# Add your import statements here
from nltk.tokenize import sent_tokenize

class SentenceSegmentation():

    def naive(self, text):

        period = [i for i in range(len(text)) if (i == len(text)-1) or ((text.startswith(".", i) or text.startswith("!", i) or text.startswith("?", i)) and text[i+2].isupper)] 
        
        segmentedText = []
        i = 0
        for d in period:
            segmentedText.append(text[i:d+1])
            i = d+2  

        return segmentedText

    def punkt(self, text):
        
        segmentedText = sent_tokenize(text)

        return segmentedText