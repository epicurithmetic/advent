# Advent of Code 2022 :: Day 02

# Read in the data 
game_data_file = open("day02-data.txt","r")
game_data = game_data_file.read()
game_data_file.close()
game_data = game_data[:-1]
game_data = game_data.split("\n")

# Some functions to determine the points per game.
def points_for_choice(choice):

    if choice == "X":
        # X stands for rock
        return 1
    elif choice == "Y":
        # Y stands for paper
        return 2
    else:
        # Z stands for scissors.
        return 3

def points_for_game(opponent,me):

    if opponent == "A":
        # A stands for rock
        if me == "X":
            # X stands for rock: tie
            return 3
        elif me == "Y":
            # Y stands for paper: win
            return 6
            # Z stands for scissors: loss
        else:
            return 0
    
    elif opponent == "B":
        # B stands for paper
        if me == "X":
            # X stands for rock: loss
            return 0
        elif me == "Y":
            # Y stands for paper: tie
            return 3
            # Z stands for scissors: win
        else:
            return 6

    else:
        # C stands for scissors
        if me == "X":
            # X stands for rock: win
            return 6
        elif me == "Y":
            # Y stands for paper: loss
            return 0
            # Z stands for scissors: tie
        else:
            return 3  


def score_calculator_two(opponent,result):

    if opponent == "A":
        # A stands for rock
        if result == "X":
            # X stands for loss: so I go scissors
            return 0 + 3
        elif result == "Y":
            # Y stands for tie: so I go rock
            return 3 + 1
            # Z stands for win: so I go paper
        else:
            return 6 + 2

    elif opponent == "B":
        # B stands for Paper
        if result == "X":
            # X stands for loss: so I go rock
            return 0 + 1
        elif result == "Y":
            # Y stands for tie: so I go paper
            return 3 + 2
            # Z stands for win: so I go scissors
        else:
            return 6 + 3
    
    else:
        # C stands for scissors
        if result == "X":
            # X stands for loss: so I go paper
            return 0 + 2
        elif result == "Y":
            # Y stands for tie: so I go scissors
            return 3 + 3
            # Z stands for win: so I go rock
        else:
            return 6 + 1
# Initialise point total
total_points = 0

# Loop through the games
for game in game_data:
    
    game_score = 0
    
    opponent_choice = game[0]
    my_choice = game[2]

    # game_score += points_for_choice(my_choice)
    # game_score += points_for_game(opponent_choice,my_choice)

    # total_points += game_score

    total_points += score_calculator_two(opponent_choice,my_choice)

print(total_points)

    

