#RockPaperScissprs
print('Welcome to Rock, Paper, Scissors! what is your name?')
player_name = input().capitalize()
player_score = 0
comp_score = 0
StillPlayin = 1
while StillPlayin != "0":
    possible_moves = ['Rock', 'Paper', 'Scissors']
    while True:
        player_move = ""
        comp_move = ""

        print("It\'s your turn...")
        print("Rock, Paper, Scissors?")
        player_move = input().upper()
        if player_move.startswith("R"):
            player_move = "Rock"
        if player_move.startswith("P"):
            player_move = "Paper"
        if player_move.startswith("S"):
            player_move = "Scissors"

        import random
        comp_move = random.choice(possible_moves)
        print()
        print(f'Player selected: {player_move}')
        print(f'Computer selected: {comp_move}')
        print()

        if player_move == comp_move:
            print("Game Tied!")
            break

        elif player_move == "Rock":
            if comp_move == "Scissors":
                print('Game Won!')
                player_score += 1
                break
            else:
                print("Game Lost!")
                comp_score += 1
                break

        elif player_move == "Paper":
            if comp_move == "Rock":
                print('Game Won!')
                player_score += 1
                break
            else:
                print("Game Lost!")
                comp_score += 1
                break

        elif player_move == "Scissors":
            if comp_move == "Paper":
                print('Game Won!')
                player_score += 1
                break
            else:
                print("Game Lost!")
                comp_score += 1
                break

    print(f' {player_name} is on: {player_score}')
    print(f' Computer is on: {comp_score}')
    if player_score == comp_score:
        print("The game is Tied!")
    elif player_score > comp_score:
        print()
        print(f'{player_name} is winning!')
    else:
        print()
        print(f'{player_name} is losing!')

    print("Do you want to keep playing? press any key. press 0 to exit")
    StillPlayin = input()
print(player_name, "score is ", player_score)
print("Computer score is ", comp_score)
if player_score > comp_score:
  print(f'{player_name} Won!')
else:
  print("Computer Won!")
