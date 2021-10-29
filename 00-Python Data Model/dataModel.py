"""
You can think of data model as a description of python as Framework.it formalizes the interfaces of the building blocks
of the language itself, such as sequences, functions, iterators, classes, text manages. and so on.


when we using a framework we spend a lot of time coding methods  that are called by the frameworl, the same appens when
we leverage the python data model to build new class



the python interpreter invokes special methods to perfom basic operations


ex: obj[key] is suported by the __getitem__() special method.  in order to evaluate my_collection[key], the interpreter calls
my_collection.__getitem__(key)



How special methods are used 


the first thing to know about special methods is that they are meant to be called by the  python  interpreter, and not by you, you write len(my_object)

if my object is any istance of  a user-defined class, the python calls the __len__ method you implemented
"""


from collections import namedtuple
import math


card = namedtuple("card", ["rank", "suit"])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()


    def __init__(self) -> None:
        self._cards = [card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]


    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]




class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x!r} , {self.y!r})"
    
    def __obs__(self):
        return math.hipot(self.x, self.y)
    
    def __bool__(self):
        return bool(self)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y

        return Vector(x, y)
    

    def __mul__(self, scalar):
        return Vector(self.x *scalar , self.y *scalar)




def spade_high(card):

    suit_values = dict(spades = 3, hearts = 2, diamonds= 1, clubs= 0)
    rank_values = FrenchDeck.ranks.index(card.rank)
    return rank_values * len(suit_values) + suit_values[card.suit]


def main():
    deck = FrenchDeck()
    print(len(deck))
    print(deck[0])
    print(deck[-1])
    print(deck[12::13])
    print(deck[:6])

    """just by implementing the __getitem__ special method, our deck is also interable"""


    for card in deck:
        print(card)
    
    """for card in reversed(deck):
        print(card)"""
    
    """card2 = card("Q", "hearts")
    print(card2 in deck)"""


    for card in sorted(deck, key=spade_high):
        print(card)


    v = Vector(34, 3)
    print(v)
    v1 = Vector(0, 6)
    v2 = Vector(2, 2)
    print(v1 +  v2)

   



if __name__ == "__main__":
    main()
        