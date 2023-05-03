import random

# scoreboard
sb_win = (0)
sb_loss = (0)
sb_draw = (0)

#loop
play_again="y"
while play_again == "y" :

    #user input
    user_move = input("Enter a choice (rock, paper, scissors): ")
    input_error = "false"
    if user_move not in ("rock", "paper", "scissors"):
        print("\nERROR! Please enter selection exactly as shown above.\n")
        input_error = "true"

    #random pc play
    possible_moves = ["rock", "paper", "scissors"]
    computer_move = random.choice(possible_moves)

    #print results of actions or error message
    if input_error == "true":
        print("Try again.")
    else: print(f"\nYou chose {user_move}, computer chose {computer_move}.\n")

    #judging
    if user_move == computer_move:
        print(f"IT's a DRAW!")
        sb_draw += 1
    elif user_move == "rock":
        if computer_move == "scissors":
            print("Rock smashes scissors! You win!")
            sb_win += 1
        else:
            print("Paper covers rock! You lose...")
            sb_loss += 1
    elif user_move == "paper":
        if computer_move == "rock":
            print("Paper covers rock! You win!")
            sb_win += 1
        else:
            print("Scissors cuts paper! You lose...")
            sb_loss += 1
    elif user_move == "scissors":
        if computer_move == "paper":
            print("Scissors cuts paper! You win!")
            sb_win += 1
        else:
            print("Rock smashes scissors! You lose...")
            sb_loss += 1

    #print score
    print ("Win, Loss, Draw")
    print(sb_win,sb_loss,sb_draw)

    play_again = input("play again? (y/n): ")
    if play_again.lower() != "y":
        break