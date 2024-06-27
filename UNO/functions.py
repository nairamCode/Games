import random

class game_setup:
    # Player_setup function is used to create the players at the start of the game
    def player_setup():
        # Input the amount of players participating
        player_count = int(input("Input player count: "))
        while player_count > 10 or player_count < 2:
            player_count = int(input("Input player count: "))
        # Create an universal player list
        player_list = []
        # Iterate through the player count to create every player
        for i in range(0,player_count):
            # Create a player to store additional information within
            player = []
            # Input player name and give him a hand for his cards
            player_set_name = input("Input player name: ")
            player_set_cards = []
            player_set_points = []
            # Add the information to the player
            player.append(player_set_name)
            player.append(player_set_cards)
            player.append(player_set_points)
            # Add the player to the player list
            player_list.append(player)
        random.shuffle(player_list)
        # Return the player list
        return player_list

    # Deal_cards function is used to deal the cards to the players at the start of the game
    def deal_cards(player_list):
        # Create a deck to deal cards from and to play with later
        deck = ["red_0", "yellow_0", "green_0", "blue_0", "red_0", "yellow_0", "green_0", "blue_0", "red_1", "yellow_1", "green_1", "blue_1", "red_1", "yellow_1", "green_1", "blue_1", "red_2", "yellow_2", "green_2", "blue_2", "red_2", "yellow_2", "green_2", "blue_2", "red_3", "yellow_3", "green_3", "blue_3", "red_3", "yellow_3", "green_3", "blue_3", "red_4", "yellow_4", "green_4", "blue_4", "red_4", "yellow_4", "green_4", "blue_4", "red_5", "yellow_5", "green_5", "blue_5", "red_5", "yellow_5", "green_5", "blue_5", "red_6", "yellow_6", "green_6", "blue_6", "red_6", "yellow_6", "green_6", "blue_6", "red_7", "yellow_7", "green_7", "blue_7", "red_7", "yellow_7", "green_7", "blue_7", "red_8", "yellow_8", "green_8", "blue_8", "red_8", "yellow_8", "green_8", "blue_8", "red_9", "yellow_9", "green_9", "blue_9", "red_9", "yellow_9", "green_9", "blue_9", "red_stop", "yellow_stop", "green_stop", "blue_stop", "red_stop", "yellow_stop", "green_stop", "blue_stop", "red_switch", "yellow_switch", "green_switch", "blue_switch", "red_switch", "yellow_switch", "green_switch", "blue_switch", "red_draw2", "yellow_draw2", "green_draw2", "blue_draw2", "red_draw2", "yellow_draw2", "green_draw2", "blue_draw2", "black_color", "black_color", "black_color", "black_color", "black_draw4", "black_draw4", "black_draw4", "black_draw4"]
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
        random_card = random.randint(0,len(deck)-1)
        while deck[random_card] == "black_color" or deck[random_card] == "black_draw4":
            random_card = random.randint(0,len(deck)-1)
        discard = []
        discard.append(deck[random_card])
        deck.remove(deck[random_card])
        # Return the player list (now everyone has cards) and the deck (which now has less cards)
        return player_list, deck, discard

def check_last_card(stapel):
    if len(stapel) == 0:
        return None, None
    else:
        last_card = stapel[-1]
        x = last_card.split("_")
        color = x[0]
        action = x[1]
        return color, action
    
def check_for_win(player_list):
    for i in range(0,len(player_list)):
        player = player_list[i]
        player_hand = player[1]
        if len(player_hand) == 0:
            return True
        else:
            return False

def do_last_action(player_list, deck, last_color, last_action):
    numbers = ["0", "1", "2", "3","4","5","6","7","8","9"]
    if last_action == None or last_action in numbers:
        return player_list, deck, last_color, last_action
    elif last_action == "draw2":
        player_list, deck = draw_cards(deck, player_list, 2)
        player_list = next_turn(player_list)
        return player_list, deck, last_color, last_action
    elif last_action == "draw4":
        player_list, deck = draw_cards(deck, player_list, 4)
        colors = ["red", "yellow", "green", "blue"]
        last_color = input("Chose next color: ")
        while last_color not in colors:
            print("Your Options: red, yellow, green, blue")
            last_color = input("Chose next color: ")
        player_list = next_turn(player_list)
        return player_list, deck, last_color, last_action
    elif last_action == "switch":
        player_list = player_list[::-1]
        player_list = next_turn(player_list)
        return player_list, deck, last_color, last_action
    elif last_action == "stop":
        player_list = next_turn(player_list)
        player = player_list[-1]
        print(f"The player {player[0]} was skipped.")
    return player_list, deck, last_color, last_action
    
def draw_cards(deck, player_list, amount):
    for i in range(0,amount):
            random_card = random.randint(0,len(deck)-1)
            player = player_list[0]
            player_hand = player[1]
            player_hand.append(deck[random_card])
            deck.remove(deck[random_card])
    print(f"{player[0]} drawed {amount} card(s).")
    print("")
    return player_list, deck

def next_turn(player_list):
    player_list.append(player_list[0])
    player_list.remove(player_list[0])
    return player_list

def cc_valid_cards(player_list, deck, player_hand, last_color, last_action):
    valid_cards = []
    for i in range(0,len(player_hand)):
        card = player_hand[i]
        x = card.split("_")
        color = x[0]
        action = x[1]
        if color == last_color or action == last_action:
            valid_cards.append(card)
    if len(valid_cards) == 0:
        draw_cards(deck, player_list, 1)
        next_turn(player_list)
        return None
    print("Here are all your valid cards: ")
    for i in range(0,len(valid_cards)):
        print(valid_cards[i])
    player_choice = int(input("Which one do you wanna play?: "))
    while player_choice < 1 or player_choice > len(valid_cards) + 1:
        player_choice = int(input("Which one do you wanna play?: "))
    return valid_cards[player_choice-1]

def play_card(player_list, discard, player_choice):
    player = player_list[0]
    player_hand = player[1]
    discard.append(player_choice)
    player_hand.remove(player_choice)