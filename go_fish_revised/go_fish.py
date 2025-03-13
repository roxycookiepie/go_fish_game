import random

#global variable 
public_message = print

class Card:
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    #called when trying to compare cards
    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit
    
    #convert class into a string, called when trying to print
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
    #making objects usable as keys in dictionaries and elements in sets
    #return a hash(a unique number) of a string
    #hashable means it has a hash value which never changes during its lifetime and can be compared to others
    #access memory in constant time by taking a hash and using has as an offset
    def __hash__(self):
        return hash(f"{self.rank}:{self.suit}")
    
    #used to compare rank of card, left hand side and right hand side
    def __lt__(self, lhs, rhs):
        lhs, rhs = (
            ({
                "Ace": "01",
                "Jack": "11",
                "Queen": "12",
                "King": "13"
            }.get(val.rank, r"{val.rank:.02}"), val.suit)
            for val in (lhs, rhs)
        )
        return lhs < rhs
        
