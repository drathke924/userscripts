class Deck:
	def __init__(self, cards):
		self.cards = cards
		
	def shuffleDeck(self):
		#splits the deck in half and adds the cards back as though riffle shuffled
		cards = self.cards
		firstHalf = cards[:int(len(cards)/2)]
		secondHalf = cards[int(len(cards)/2):]
		cards = []
		for i in range(len(secondHalf)):
			if len(firstHalf) > 0:
				cards.append(firstHalf.pop(0))
			cards.append(secondHalf.pop(0))
		self.cards = cards
			
	def drawCard(self):
		#returns the top card while removing it from the deck
		return self.cards.pop(0).reveal()
	
	def revealDeck(self):
		for i in self.cards:
			print(i.reveal())
			

class Card:
	def __init__(self, suit, value):
		self.suit = suit
		self.value = str(value)
	
	def reveal(self):
		return str(self.value) + " of " + str(self.suit) 
		
newSmallDeckOrder = Deck([Card("spades", "ace"), Card("clubs", "ace"), Card("hearts", "ace"), Card("diamond", "ace"), Card("spades", "2"), Card("clubs", "2"), Card("hearts", "2"), Card("diamonds", "2")])
print("Initial state")
newSmallDeckOrder.revealDeck()
newSmallDeckOrder.shuffleDeck()
print("Shuffled once")
newSmallDeckOrder.revealDeck()
print("Draw until empty")
while len(newSmallDeckOrder.cards) > 0:
	print(newSmallDeckOrder.drawCard())

oddSmallDeck = Deck([Card("spades", "ace"), Card("clubs", "ace"), Card("hearts", "ace"), Card("diamond", "ace"), Card("spades", "2"), Card("clubs", "2"), Card("hearts", "2"), Card("diamonds", "2"), Card("spades", 3)])
print("Initial state")
oddSmallDeck.revealDeck()
oddSmallDeck.shuffleDeck()
print("Shuffled once")
oddSmallDeck.revealDeck()
print("Draw until empty")
while len(oddSmallDeck.cards) > 0:
	print(oddSmallDeck.drawCard())
