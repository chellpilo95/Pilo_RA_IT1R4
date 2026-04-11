balance = 10500 # Initial balance set to $10,500. This variable will be updated as the user withdraws money from their account.

while True: # Loop to keep the program running until the user decides to exit
    try: # Try block to catch any input errors
        print("\n| Money Withdrawal System |\n")
        print("1. Withdraw Money")
        print("2. Check Balance")
        print("3. Exit")
      
        choice = int(input("\nEnter your choice: "))    # Get user choice and convert to integer

        if choice == 1: # If user chooses to withdraw money
            try: # Try block to catch any input errors during withdrawal process
                amount = float(input("\nEnter amount to withdraw: "))   # Get withdrawal amount and convert to float. Float is used to allow for decimal amounts, such as $50.75.

                if amount > balance:
                    print("Insufficient funds!") # If the withdrawal amount exceeds the current balance, an insufficient funds message will be displayed and the user will be given options to re-enter the amount, check their balance, or exit the system.

                    while True: # Loop to allow user to choose options after insufficient funds message
                        print("\nOptions:\n1. Re-enter amount\n2. Check balance\n3. Exit")

                        option = int(input("\nEnter your choice: ")) 

                        if option == 1:# Re-enter amount option. Sufficient funds will be checked again in the next iteration of the loop.
                            break   # Break to exit the options loop and return to the main withdrawal process where the user can enter a new amount.
                        elif option == 2:
                            print(f"\nCurrent balance: {balance}") # Display current balance to the user so they can decide on a new amount to withdraw.
                        elif option == 3:
                            print("Exiting system...")
                            exit() # Exit the program immediately if the user chooses to exit from the options menu.
                        else: # Invalid option handling for the options menu. If the user enters an invalid option, they will be prompted to try again without exiting the program or the options menu.
                            print("\nInvalid option. Try again.")

                elif amount <= 0: # Check for non-positive withdrawal amounts. If the user enters an amount that is zero or negative, they will be prompted to enter a valid amount greater than zero.
                    print("\nAmount must be greater than 0.")

                else: # If the withdrawal amount is valid and there are sufficient funds, the amount will be deducted from the balance and a success message will be displayed along with the remaining balance.
                    balance -= amount  # Deduct the withdrawal amount from the balance
                    print(f"\nWithdrawal successful! Your remaining balance is: {balance}")  # Display the remaining balance after a successful withdrawal

            except ValueError: # Catch any errors that occur during the withdrawal process, such as entering a non-numeric value for the amount. The user will be prompted to enter a valid number without crashing the program.
                print("\nInvalid input! Please enter a valid number.")

        elif choice == 2: # If user chooses to check balance, the current balance will be displayed.
            print(f"\nCurrent balance: {balance}")

        elif choice == 3: # If user chooses to exit, a thank you message will be displayed and the loop will break to end the program.
            print(f"\nThank you for using the system!")
            break

        else:
            print("\nInvalid choice. Please select 1-3.")

    except ValueError: # Catch any errors that occur when the user enters their choice for the main menu. If the user enters a non-numeric value, they will be prompted to enter a valid number without crashing the program.
        print("\nInvalid input! Please enter a number.")