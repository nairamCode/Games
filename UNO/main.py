from functions import *
'''# Input the amount of players participating
player_count = int(input("Input player count: "))

# Send the player count to the player setup function to create the player
player_list = player_setup(player_count)

# Create a deck to deal cards from and to play with later
deck = ["red_0", "yellow_0", "green_0", "blue_0", "red_1", "yellow_1", "green_1", "blue_1", "red_1", "yellow_1", "green_1", "blue_1", "red_2", "yellow_2", "green_2", "blue_2", "red_2", "yellow_2", "green_2", "blue_2", "red_3", "yellow_3", "green_3", "blue_3", "red_3", "yellow_3", "green_3", "blue_3", "red_4", "yellow_4", "green_4", "blue_4", "red_4", "yellow_4", "green_4", "blue_4", "red_5", "yellow_5", "green_5", "blue_5", "red_5", "yellow_5", "green_5", "blue_5", "red_6", "yellow_6", "green_6", "blue_6", "red_6", "yellow_6", "green_6", "blue_6", "red_7", "yellow_7", "green_7", "blue_7", "red_7", "yellow_7", "green_7", "blue_7", "red_8", "yellow_8", "green_8", "blue_8", "red_8", "yellow_8", "green_8", "blue_8", "red_9", "yellow_9", "green_9", "blue_9", "red_9", "yellow_9", "green_9", "blue_9", "red_stop", "yellow_stop", "green_stop", "blue_stop", "red_stop", "yellow_stop", "green_stop", "blue_stop", "red_switch", "yellow_switch", "green_switch", "blue_switch", "red_switch", "yellow_switch", "green_switch", "blue_switch", "red_draw2", "yellow_draw2", "green_draw2", "blue_draw2", "red_draw2", "yellow_draw2", "green_draw2", "blue_draw2", "black_color", "black_color", "black_color", "black_color", "black_draw4", "black_draw4", "black_draw4", "black_draw4"]

# Send th player list and deck to the deal_cards function which deals cards to the players
player_list, deck = deal_cards(player_list, deck)'''

stapel = []

last_action = check_last_card(stapel)
print(last_action)

if last_action == None:
    # Play any card
    pass
else:
    do_last_action(last_action)