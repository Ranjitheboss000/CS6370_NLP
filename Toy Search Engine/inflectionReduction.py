from util import *

from nltk.stem import WordNetLemmatizer


class InflectionReduction:

	def reduce(self, text):
		lemmatizer = WordNetLemmatizer() 
		reducedText = [[lemmatizer.lemmatize(j) for j in i] for i in text]

		return reducedText
