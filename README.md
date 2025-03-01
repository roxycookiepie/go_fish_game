# go_fish_game

#The game involves four player: the user, and other three players.

#In the card.py file:
#A class is created to store cards in ranks and suits.
#__eq__ is used to compare card ranks. The function is called when the main file compares cards using "is in" or "is not in". 
#__str__ to print out cards in "rank of suit" format, this function will be called when "print" is called in the main file.
#__lt__ is used to compare the ranks of the cards in player's hand and sort cards based on the rank. This function is called when "sorted" is called in the main file.

#count.py is a file that contians loose functions.
#The count function is for counting scores of each player. 
#draw_card function for users to draw cards from the pool if no more cards in hand
#count_players function stores how many available players are in the game. Availble player means players that still have cards in their hands, otherwise, the player is done with the game.

#In the main file go_fish.py:
#The main function is to loop through the game until all players run out of cards in their hand
#
