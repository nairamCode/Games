import random

# Player_setup function is used to create the players at the start of the game
def player_setup(player_count):
    # Create an universal player list
    player_list = []
    # Iterate through the player count to create every player
    for i in range(0,player_count):
        # Create a player to store additional information within
        player = []
        # Input player name and give him a hand for his cards
        player_set_name = input("Input player name: ")
        player_set_cards = []
        # Add the information to the player
        player.append(player_set_name)
        player.append(player_set_cards)
        # Add the player to the player list
        player_list.append(player)
    # Return the player list
    return player_list

# Deal_cards function is used to deal the cards to the players at the start of the game
def deal_cards(player_list, deck):
    # Iterate through all the players in the player list
    for i in range(0,len(player_list)):
        # Iterate 7 times because every player gets 7 cards
        for j in range(0,7):
            # Pick a random card from the deck
            random_card = random.randint(0,len(deck)-1)
            # Find the players hand
            player = player_list[i]
            player_hand = player[1]
            # Add the random card to the players hand
            player_hand.append(deck[random_card])
            # Remove the card from the deck
            deck.remove(deck[random_card])
    # Return the player list (now everyone has cards) and the deck (which now has less cards)
    return player_list, deck