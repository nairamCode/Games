from functions import *
import os

# Setup everything
player_list = game_setup.player_setup()
player_list, deck, discard, last_color = game_setup.deal_cards(player_list)
os.system('cls')

# Game loop
while True:
    last_color, last_action = check_last_card(discard, last_color)
    
    # Check win condition
    if check_for_win(player_list) == True:
        break

    # do last action
    player_list, deck, last_color, last_action = do_last_action(player_list, deck, last_color, last_action)
    
    # play
    player_hand = player_list[0][1]
    print(f"The next player is {player_list[0][0]} ({len(player_list[0][1])}).")
    print(f"The last card was a {last_color} {last_action}.", end="\n\n")

    print(input("Press any key too start:"))

    player_choice = cc_valid_cards(player_list, deck, player_hand, last_color, last_action)
    if player_choice == None:
        continue
    
    last_color = play_card(player_list, discard, player_choice, last_color)
    
    next_turn(player_list)
    #print("")
    os.system('cls')