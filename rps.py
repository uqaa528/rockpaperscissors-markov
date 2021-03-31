import numpy as np
import random

figures = np.array(["R", "P", "S"])
choices_as_numbers = np.array([0, 1, 2])

def convert_figure_to_number(figure_identifier):
    return np.where(figures == figure_identifier)[0][0]

def decide_winner(player1_choice, player2_choice, player1_label, player2_label):
    if player1_choice == player2_choice:
        return "draw"

    player1_choice = choices_as_numbers[player1_choice - 1]

    return player1_label if player1_choice == player2_choice else player2_label

choice = input("Input your choice: ")

bot_choice = random.randint(0, 2)
player_choice = convert_figure_to_number(choice)

print("bot:", figures[bot_choice])
print("player:", figures[player_choice])

print(decide_winner(player_choice, bot_choice, "player", "bot"))