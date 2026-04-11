amount_balance = 10500  

def menu():   
    print("\n| Money Withdrawal System |\n")
    print("1. Withdraw Money\n2. Check Balance\n3. Exit")
    return input("\nEnter your choice: ")

def withdraw(amount_balance):  
    try:  
        amount = float(input("\nEnter amount to withdraw: "))
        if amount <= 0:
            print("\nAmount must be greater than 0.")
        elif amount > amount_balance:
            print("\nInsufficient funds!")
            
            while True:
                option = input("\nOptions:\n1. Re-enter amount\n2. Check balance\n3. Exit\n\nEnter your choice: ")
                if option == "1": return amount_balance
                elif option == "2": print(f"\nYour Current balance is {amount_balance}.")
                elif option == "3": exit("\nExiting system...")
                else: print("\nInvalid option! Please try again.")
        else:
            amount_balance -= amount
            print(f"\nWithdrawal successful! Your remaining balance is {amount_balance}.")
            
    except ValueError:
        print("\nInvalid input! Please enter a valid number.")
        
    return amount_balance

while True:
    choice = menu()
    if choice == "1":
        amount_balance = withdraw(amount_balance)
    elif choice == "2":
        print(f"\nYour Current balance is {amount_balance}.")
    elif choice == "3":
        print("\nExiting...Thank you for using the system!")
        break
    else:
        print("\nInvalid choice! Please select 1-3.")
