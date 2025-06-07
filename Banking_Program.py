def showbalance(balance):
    print("****************************")
    print(f"your account balance is {balance} rs")

def deposit():
    print("****************************")
    amount = int(input("Enter the amount to be deposited : "))
    
    if amount < 0:
        print("Enter a valid amount.")
        return 0
    
    else :
        return amount

def withdraw(balance):
    print("****************************")
    amount = int(input("Enter amount to withdraw : "))

    if amount > balance:
        print("Insufficient balance.")
        return 0
    elif amount < 0:
        print("Amount should be greater than 0.")
        return 0
    else:
        return amount

def main():
    balance = 0.00

    while True:
        print("****************************")
        print("      Banking Program       ")
        print("****************************")
        print("1.Balance Enquiry")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("****************************")
        choice = input("Enter your choice(1-4):")
        match choice:
            case "1" :
                showbalance(balance)
            case "2" :
                balance +=deposit()
            case "3" :
                balance -= withdraw(balance)
            case "4" :
                break
            case _:
                print("Invalid choice! Enter a valid choice.")
    
    print("Thank you! Have a nice day.")

if __name__ == "__main__":
    main()