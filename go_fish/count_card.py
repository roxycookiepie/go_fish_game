def count(card_deal, player, card, score):
    #count # of card that has the same rank in your list
    sum = card_deal[player].count(card.rank)
    #if you have 4 cards with the same rank, remove these four cards and add a point to the score
    if sum == 4:
        print(f"{player.capitalize()} got four {card.rank}s in hand!")
        score += 1 
        print(f"{player.capitalize()} earned a point!")
        print(f"Total score of {player.capitalize()}: {score}")
        for i in range(4):
            card_deal[player].remove(card)
            i += 1      
    return score

def draw_card(hand, pool, n):
    available_card = min(n, len(pool))
    if len(pool) != 0:
        for _ in range(available_card):
            get_card = pool[-1]
            hand.append(get_card)
            pool.pop()
            print(f"Drawing a card from the pool...\n")
    else:
        print("There are no more cards in the pool")
    return hand
        
def count_players(card_deal):
    select_players = []
    for player in card_deal:
        if len(card_deal[player]) != 0:
            select_players.append(player)
    return select_players
