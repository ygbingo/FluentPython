import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA") + ["Joker"]
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self) -> None:
        self._cards = [Card(rank, suit) for rank in self.ranks[:-1]
                                        for suit in self.suits]
        self._cards.extend([Card('Joker', 'black'), Card('Joker', 'red')])
        
    def __len__(self) -> int:
        return len(self._cards)
    
    def __getitem__(self, position) -> Card:
        return self._cards[position]
    

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0, red=5, black=4)

def spades_high(card: Card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]
    

if __name__=="__main__":
    beer_card = Card('7', 'diamonds')
    print(beer_card)

    deck = FrenchDeck()
    print(len(deck))
    print(deck[0])
    print(deck[-1])
    print(choice(deck))

    for card in sorted(deck, key=spades_high):
        print(card)