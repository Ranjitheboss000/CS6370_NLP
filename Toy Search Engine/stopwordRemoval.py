from util import *

from nltk.corpus import stopwords

class StopwordRemoval():

	def fromList(self, text):

		stop_words = stopwords.words('english')

		stopwordRemovedText = [[w for w in tok_sen if not w in stop_words] for tok_sen in text]

		return stopwordRemovedText




	