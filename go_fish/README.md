# go_fish_game
	
## Go fish game rules
<ol>
<li>The game involves four player: the user, and other three players.<br>
<li>Go_Fish starts with appending 5 cards from pool to each player's hand.<br>
<li>The player gets to select another player to get card from if the selected_player still has card in their hand. Otherwise, the player need to select another player again.<br>
<li>If the selected_player has card in hand, player gets to select a card from the selected_player by entering the rank of the card. The player must have a card that has the same rank in hand, otherwise, it will output an error and ask the player to select another card that is in hand.<br>
<li>If all requirements are satisfied, the program will compare if the selected_card is in the selected_player's hand.<br> 
<li>If selected_card(s) are in selected_player's hand, append all cards that have the same rank in player's hand, and remove card(s) from the selected_player's hand.<br> 
<li>The player gets to continue playing the game by selecting another player and another card in hand.<br>
<li>If selected_card not in selected_player's hand, the player gets a random card from the pool. The player's round ends.<br>
<li>After getting each card either from the pool or from another player, the programs counts if there are four cards that have the same rank in player's hand. If so, the four cards are removed from players hand, and player earns one point.<br>
<li>If any player runs out of card in hand during the round, the player get two random cards from the pool. If there are no cards in the pool, then the players who have empty hand have finished their game. The game goes on until all players have no cards in their hands.
</ol>

## card.py
<ul><li>A class is created to store cards in ranks and suits.<br>
<li>__eq__ is used to compare card ranks. The function is called when the main file compares cards using "is in" or "is not in".<br> 
<li>__str__ to print out cards in "rank of suit" format, this function will be called when "print" is called in the main file.<br>
<li>__lt__ is used to compare the ranks of the cards in player's hand and sort cards based on the rank. This function is called when "sorted" is called in the main file.<br>
</ul>

## count.py
<ul><li>A file that contians loose functions.<br>
<li>The count function is for counting scores of each player.<br> 
<li>draw_card function for users to draw cards from the pool if no more cards in hand.<br>
<li>count_players function stores how many available players are in the game. Availble player means players that still have cards in their hands, otherwise, the player is done with the game.<br>
</ul>

## go_fish.py (main file)
<ul><li>The main function is to loop through the game until all players run out of cards in their hands.<br>
<li>The game starts with the user's round, which is calling the you_round function.<br>
<li>you_round gets input from user. Once the user's round is finished, the game will continue with other players round.<br>
<li>other_players function autogenerates other players' rounds by selecting random players to get card from and selecting random cards that are in hand.<br> 
<li>Once the game ends, the program will output the player with the highest score as the winner.
</ul>
