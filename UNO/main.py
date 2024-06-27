from functions import *

# Send the player count to the player setup function to create the player
player_list = game_setup.player_setup()
player_list, deck, discard = game_setup.deal_cards(player_list)

for i in range(0,len(player_list)):
    print(player_list[i])

while True:
    last_color, last_action = check_last_card(discard)
    # Check win condition
    if check_for_win(player_list) == True:
        break
    # do last action
    player_list, deck, last_color, last_action = do_last_action(player_list, deck, last_color, last_action)
    # play
    player = player_list[0]
    player_name = player[0]
    player_hand = player[1]
    print(f"The next player is {player_name}.")
    print(f"The last card was a {last_color} {last_action}.")

    player_choice = cc_valid_cards(player_list, deck, player_hand, last_color, last_action)
    if player_choice == None:
        continue
    play_card(player_list, discard, player_choice)
    next_turn(player_list)

    print("")