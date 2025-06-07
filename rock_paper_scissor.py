import random
option = ("rock","paper","scissor")

while True:
    player = input("Enter your choice(rock/paper/scissor) : ")
    computer = random.choice(option)
    if player not in option:
        print("Invalid choice!")
        player = input("Enter your choice(rock/paper/scissor) : ")
    else:    
        print(f"Player : {player}")
    print(f"Computer : {computer}")

    if computer == player:
        print("It's a tie!")
    elif player == "rock" and computer == "scissor":
        print("You win!")
    elif player == "scissor" and computer == "paper":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    else:
        print("You lose!")
    
    if not input("Play again(y/n)?: ").lower() == "y":
        break

print("Thanks for Playing")