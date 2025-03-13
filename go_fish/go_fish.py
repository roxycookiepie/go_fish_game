import random    
from card import Card
from count_card import count, draw_card, count_players

#make an empty list for deck.
deck = []

#Keep track of player's score
score = {
    "you": 0,
    "Jack": 0,
    "Lisa": 0,
    "Mike": 0
}

def main():  
    #append 52 cards in deck[], now the list has 52 cards.
    global deck
    deck = get_deck(deck)
    #deal cards and assign five cards to each player
    card_deal = deal(deck)
    you_round(card_deal)
    while True:
        print("Scores:")
        print(score)
        players = count_players(card_deal)
        print(players)
        print(len(players))
        if len(players) == 0:
            winner = max(score, key = score.get)
            print(f"The winner is: {winner.capitalize()}!")
            break
        elif len(card_deal["you"]) != 0:
            you_round(card_deal)
        else:
           other_players(card_deal)
            

#This function is used to generate 52 cards and store in the deck[] list.
def get_deck(deck): 
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    for suit in suits:
        for rank in ranks:
            #call the Class Card, store values as rank and suit
            deck.append(Card(rank, suit))
            
    #return the deck list with 52 cards
    return deck


#This function is used to play the game
def deal(deck):
    global pool
    pool = deck

    global card_deal
    card_deal = {
        "you": [],
        "Jack": [],
        "Lisa": [],
        "Mike":[],
    }

    random.shuffle(pool)

    for hand in card_deal.values():
        #Slice the first 5 cards and store the cards in card_deal.values 
        hand.extend(pool[:5])
        #Slice the cards after the first 5 cards store in pool
        pool = pool[5:]

    return card_deal

def you_round(card_deal):
    global score
    player = "you"
    while len(card_deal[player]) != 0:
        print("")
        #display cards in you's hand
        print("You have these cards in hand: ")
        #call __str__ function in class Card and print out list as rank of suits, use * to print string, otherwise, program prints memory address
        print(*sorted(card_deal[player]), sep = ", ")
        print("")
        
        #if the you still has cards in their hand, ask you to pick a player to get card from
        while True:
            print("1) Jack")
            print("2) Lisa")
            print("3) Mike", "\n")
            select_player = input("Select a player you would like to get a card from by entering the number: ")

            if select_player == "1":
                select_player = "Jack"
                #For testing
                #print(*sorted(card_deal[select_player]), sep = ", ")
                break          
            elif select_player == "2":
                select_player = "Lisa"
                #For testing
                #print(*sorted(card_deal[select_player]), sep = ", ")
                break               
            elif select_player == "3":
                select_player = "Mike"
                #For testing
                #print(*sorted(card_deal[select_player]), sep = ", ")
                break
            #if the you enter something that is not "!", "2", "3", output an error message and prompt the you for input again
            else:
                print("Invalid input, please select player by entering 1, 2, or 3\n")      

        if len(card_deal[select_player]) == 0:
            print("Chosen player has no card in hand, please choose another player.")
            continue

        #if the selected player still has card in their hands
        while len(card_deal[select_player]) != 0:
            #make pool a global variable
            global pool

            #ask uesr to pick a card from another player by entering the rank of the card
            #make all you input lower case, then capitalize to make you input case insensitive
            select_card = input("Please select a card you would like to get from chosen player by entering the rank of the card: ")
            select_card = select_card.lower().capitalize()
            
            #call Class function __eq__ to compare if you's input(string) is in self(card in you's hand, stored as a string in card_deal dictionary)
            if select_card not in card_deal[player]:
                print("")
                print("Error! You must pick a card that is in your hand.\n")
                #print the cards in you's hand again for reference
                print("You have these cards in hand: ")
                print(*sorted(card_deal[player]), sep = ", ")
                print("")
                continue

            if select_card not in card_deal[select_player]:
                if len(pool) != 0:
                    print("")
                    #if card not in chosen player's hand
                    print("Go fish")
                    #get a card from pool and append to you's hand, remove card from pool
                    get_card = pool[-1]
                    card_deal[player].append(get_card)
                    pool.pop()

                    print(f"You have gotten {get_card} from the pool\n")
                    score[player] = count(card_deal, player, get_card, score[player])
                else:
                    print("No card in pool. game continues...\n")

                print("You have these cards in hand:")
                print(*sorted(card_deal[player]), sep = ", ")
                print("")
                #your round ends
                other_players(card_deal)
                return 
            #create a temporary list for select_player's hand so the list does not skip index while iterating
            temp_hand = card_deal[select_player].copy()
            for card in card_deal[select_player]:
                if card == select_card:
                    card_deal["you"].append(card)
                    #remove the card from chosen player's hand
                    temp_hand.remove(card)
                    print("")
                    print(f"You have gotten {card} from {select_player}'s hand!")
                #if player has 4 cards that has the same rank, call the count card function
                    score[player] = count(card_deal, player, card, score[player])
            card_deal[select_player] = temp_hand

            if len(card_deal[player]) == 0:
                card_deal[player] = draw_card(card_deal[player], pool, 2)
                if len(card_deal[player]) == 0:
                    print(f"{player.capitalize()} have finished the game.\n")

            if len(card_deal[select_player]) == 0:
                card_deal[select_player] = draw_card(card_deal[select_player], pool, 2)
                if len(card_deal[select_player]) == 0:
                    print(f"{select_player} has finished the game.\n")
                    print(f"Score of {select_player}: {score[select_player]}")
            break 
    return   
                       
                
def other_players(card_deal):
    global score
    for player in card_deal:
        #skip the you round, defined in you_round function
        if player == "you":
            continue
        if len(card_deal[player]) == 0:
            continue
        while len(card_deal[player]) != 0:
            select_players = count_players(card_deal)
            if len(select_players) == 0:
                return
            #pick a player to choose card from, but cannot be player themselves.
            select_player = random.choice([p for p in select_players if p != player])
            select_card = random.choice(card_deal[player]).rank
            
            print(f"{player} is asking a {select_card} from {select_player}.\n")

            if select_card not in card_deal[select_player]:
                if len(pool) != 0:
                    print("Go fish")
                    print("")
                    card = pool.pop()
                    card_deal[player].append(card)
                    print(f"{player} has gotten a card from the pool.\n")
                    score[player] = count(card_deal, player, card, score[player])
                else:
                    print("No card in pool. game continues...\n")
                break
            
            if len(card_deal[select_player]) == 0:
                print("Chosen player has no card in hand, please choose another player.")
                continue
            #make a temporary list. iterate over the temporary copy list because removing card from original list will modity the select_player's list
            #iterate over modified select_players list will result in skipping index
            player_list = card_deal[select_player].copy()
            for card in player_list:
                if card == select_card:
                    card_deal[player].append(card)
                    print(f"{player} has gotten a {card} from {select_player}.\n")
                    #remove the card from chosen player's hand
                    card_deal[select_player].remove(card)
                score[player] = count(card_deal, player, card, score[player])
            if len(card_deal[player]) == 0:
                if len(pool) == 0:
                    print(f"{player} has finished the game.\n")
                else:
                    card_deal[player] = draw_card(card_deal[player], pool, 2)
                    print(card_deal[player])
            if len(card_deal[select_player]) == 0:
                if len(pool) == 0:
                    print(f"{select_player} has finished the game.\n")
                    print(f"Score of {select_player}: {score[select_player]}")
                else:
                    card_deal[select_player] = draw_card(card_deal[select_player], pool, 2)
                    print(card_deal[select_player])
    return  
                          

if __name__ == "__main__":
    main()
