import random

def spin():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']

    return [random.choice(symbols) for _ in range(3)]

def print_result(row):
    print(" ".join(row))

def payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 3
        elif row[0] == "🍉":
            return bet * 5
        elif row[0] == "🍋":
            return bet * 10
        elif row[0] == "🔔":
            return bet * 20
        elif row[0] == "⭐":
            return bet * 25
    return 0


def main():

    balance = 100
    
    print("****************************")
    print("Welcome to Python slot game!")
    print("Symbols : 🍒 🍉 🍋 🔔 ⭐")
    print("****************************")

    while balance > 0:
        print("****************************")
        print(f"Current balance {balance} rs")
        print("****************************")
        try:
            bet = int(input("Enter the amount you want to bet : "))
        except ValueError:
            print("****************************")
            print("Enter a valid amount!")
            continue
        if bet > balance:
            print("****************************")
            print("Insufficient balance!")
            continue
        elif bet <= 0:
            print("***************************************")
            print("Bet amount should be greater than zero!")
            continue
        else:
            balance -= bet
            row = spin()
            print("**************")
            print("Spinning....\n")
            print("**************")
            print_result(row)

            get_payout = payout(row, bet)

            if get_payout > 0:
                print(f"Congratulations you won {get_payout} rs")
                balance += get_payout
                print(f"Current balance {balance} rs")
            else:
                print("Sorry! You lost this round")
                print(f"Current balance {balance} rs")
            print("*************************************")
            if balance > 0:
                if input("Would you like to play again (y/n) : ").lower() != "y":
                    break
    
    print('Thank you!')

if __name__ == "__main__":
    main()