class Deck:
	def __init__(self, cards):
		cards = []
		
	def shuffleDeck():
		firstHalf = cards[:(len(cards)/2)]
		secondHalf = cards[(len(cards)/2):]
		cards = []
		for i in range(len(secondHalf)):
			if len(firstHalf) > 0:
				cards.append(firstHalf.pop(0))
			cards.append(secondHalf.pop(0)
			

class Card:
	def __init__(self, color, suit):
		