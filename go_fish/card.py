class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def __eq__(self, other):
        #if other is a string, compare it with self(this is a card, also a string), then return True or False
        if isinstance(other, str):
            return self.rank == other

        #Compare card with another card
        return self.rank == other.rank
        
    def __str__(self):
        #print out rank of suit
        return f"{self.rank} of {self.suit}"
    
    def __lt__(self, next_card):
        rank_dict = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, 
                      "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 11, "Queen": 12, "King": 13, "Ace": 14}
        card_left = (rank_dict[self.rank], self.suit)
        card_right = (rank_dict[next_card.rank], next_card.suit)
        if card_left < card_right:
            return True
        else:
            return False
        


    
    

                 
            
            
