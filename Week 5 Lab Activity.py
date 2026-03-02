user_list = []

while True: 
    print("\n===SYSTEM MENU===\nA. List users\nB. Add new user\nC. Update a user\nD. Delete a user\nE. Exit")

    option = input("\nMy choice: ").upper()

    if option == 'A':
        print(user_list or "No users found.")

    elif option == 'B':
        user_list.append(input("New User Name: "))
        print(f"\nCurrent Users: {user_list}")

    elif option == 'C':
        old = input("Old User: ")
        if old in user_list:
            user_list[user_list.index(old)] = input("Update User: ")
            print(f"\nCurrent Users: {user_list}")
        else:
            print("User not found.")

    elif option == 'D':
        rem = input("Which user to delete: ")
        if rem in user_list: 
            user_list.remove(rem)
            print(f"\nCurrent Users: {user_list}")
        else:
            print("User not found.")

    elif option == 'E':
        break

    else:
        print("Invalid option. Please Try Again.")

print("\nExiting the system...")