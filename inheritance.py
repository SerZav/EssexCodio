import random

class Card:
  suit_name = ['clubs','diamonds','hearts','spades']
  suit_rank = [None,'Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']

  def __init__(self, suit=1, rank=2):
    self.suit = suit
    self.rank = rank

  def __str__(self):
    return self.suit_rank[self.rank] + " of " + self.suit_name[self.suit]

  def __lt__(self,other):
    #stands for less than
    if self.suit < other.suit : return True
    if self.suit > other.suit : return False
    
    #check rank
    return self.rank < other.rank

class Deck:
  def __init__(self):
    self.cards = []
    for suit in range(0,4):
      for rank in range(1,13):
        self.cards.append(Card(suit,rank))
  def __str__(self):
    list_cards = []
    for card in self.cards:
      list_cards.append(str(card))
    return '\n'.join(list_cards)
  def pop_card(self):
    return self.cards.pop()
  def add_card(self, card):
    self.cards.append(card)
  def shuffle(self):
    random.shuffle(self.cards)
  def sort(self):
    self.cards.sort()

class Hand(Deck):
  """ inherits from Deck """

card1 = Card(2,10)
card2 = Card(2,10)
print(card1)
print(card2)

# invoke the __lt__ to compare clases
print(card1 < card2)
deck1 = Deck()
deck1.shuffle()
print(deck1)
deck1.sort()
print(deck1)
newHand = Hand()
