balance = 10500  

def menu():   
    print("\n| Money Withdrawal System |\n")
    print("1. Withdraw Money\n2. Check Balance\n3. Exit")
    return input("\nEnter your choice: ")

def withdraw(balance):  
    try:  
        amount = float(input("\nEnter amount to withdraw: "))
        if amount <= 0:
            print("\nAmount must be greater than 0.")
        elif amount > balance:
            print("\nInsufficient funds!")
            
            while True:
                option = input("\nOptions:\n1. Re-enter amount\n2. Check balance\n3. Exit\n\nEnter your choice: ")
                if option == "1": return balance
                elif option == "2": print(f"\nYour Current balance is {balance}.")
                elif option == "3": exit("\nExiting system...")
                else: print("\nInvalid option! Please try again.")
        else:
            balance -= amount
            print(f"\nWithdrawal successful! Your remaining balance is {balance}.")
            
    except ValueError:
        print("\nInvalid input! Please enter a valid number.")
        
    return balance

while True:
    choice = menu()
    if choice == "1":
        balance = withdraw(balance)
    elif choice == "2":
        print(f"\nYour Current balance is {balance}.")
    elif choice == "3":
        print("\nExiting...Thank you for using the system!")
        break
    else:
        print("\nInvalid choice! Please select 1-3.")
