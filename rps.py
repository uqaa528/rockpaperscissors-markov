import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# initial setup
figures = np.array(["R", "P", "S"])
choices_as_numbers = np.array([0, 1, 2])

# occurences matrix determines how many times given figure occured after the other
# also we can use probabilities here instead of occurences.
# initial numbers are purely random
occurrences_matrix = np.array([[3, 3, 3], [3, 3, 3], [3, 3, 3]])

PLAYER_1 = "player"
PLAYER_2 = "bot"
is_game_running = True
previous_choice = 0
total_score = 0
score_list = []
counter = 0

# function that converts user input to `int` representing given figure
def convert_figure_to_number(figure_identifier):
    return np.where(figures == figure_identifier)[0][0]

# function that determines who won the game. if we look at our `figures` array we can see that
# figure of lower index is beaten by one with the higher index, also we use property of np.array
# that lets us refrence objects from the back using negative numbers so we do not encounter IndexError
def decide_winner(player1_choice, player2_choice, player1_label, player2_label):
    if player1_choice == player2_choice:
        return "draw"

    player1_choice = choices_as_numbers[player1_choice - 1]

    return player1_label if player1_choice == player2_choice else player2_label

# function that draws random number based on number of occurences of given figure after the other
def make_prediction(previous_player_choice):
    prob = [0.0, 0.0, 0.0]

    for index in range(3):
        prob[index] = occurrences_matrix[previous_choice][index] / np.sum(occurrences_matrix[previous_player_choice])
    
    return np.random.choice(choices_as_numbers, replace=True, p=prob)

# main game loop
while(is_game_running):
    choice = input("Input your choice: ")
    
    player_choice = convert_figure_to_number(choice)
    bot_choice = make_prediction(previous_choice)

    print(PLAYER_1, figures[player_choice])
    print(PLAYER_2, figures[bot_choice])

    winner = decide_winner(player_choice, bot_choice, PLAYER_1, PLAYER_2)
    
    score = 0
    if winner == PLAYER_1:
        score = -1
    if winner == PLAYER_2:
        score = 1
    
    print(winner)

    # line of code responsible for learning
    if (winner == PLAYER_1 and counter != 0):
        occurrences_matrix[previous_choice][player_choice] = occurrences_matrix[previous_choice][player_choice] + 1

    previous_choice = player_choice
    counter += 1

    total_score += score
    score_list.append(total_score)

    if counter >= 10:
        is_game_running = False

plt.plot(score_list)
plt.grid(True)
plt.ylabel("bot's score")
plt.xlabel("game no.")
plt.show()