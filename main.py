import random
while True:
    choices = ["r","p","s"]
    computer = random.choice(choices)
    player = None
    while player not in choices:
        print("NOTE Rx = ROCK , P = PAPER S = SCISSORS , ENJOY YOUR GAME")
        player = input("R,P,or S?:").lower()
    if player == computer:
        print("computer:", computer)
        print("player:", player)
        print("Tie!")
        print("Type yes to cont playing and No to end the game")

    elif player == "R":
        if computer == "P":
            print("computer:", computer)
            print("player:", player)
            print("you lose!")
            print("Type yes to cont playing and No to end the game")

        if computer == "S":
            print("computer:", computer)
            print("player:", player)
            print("you win!")
            print("Type yes to cont playing and No to end the game")

    elif player == "S":
        if computer == "R":
            print("computer:", computer)
            print("player:", player)
            print("you lose!")
            print("Type yes to cont playing and No to end the game")

        if computer == "P":
            print("computer:", computer)
            print("player:", player)
            print("you win!")
            print("Type yes to cont playing and No to end the game")

    elif player == "P":
        if computer == "S":
            print("computer:", computer)
            print("player:", player)
            print("you lose!")
            print("Type yes to cont playing and No to end the game")

        if computer == "R":
            print("computer:", computer)
            print("player:", player)
            print("you win!")
            print("Type yes to cont playing and No to end the game")

    play_again = input("play again?(yes/no):").lower()

