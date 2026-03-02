#make a progroam that can add, update, delete and list users in a list. The program should continue to run until the user chooses to exit.
#use a list to store user and a while true loop to keep the program running until the user chooses to exit. Use if-elif-else statements to handle the different options for listing, adding, updating, and deleting users.

user_list = []

while True: 
    print("\n===SYSTEM MENU===\nA. List users\nB. Add new user\nC. Update a user\nD. Delete a user\nE. Exit")

    option = input("\nMy choice: ").upper()

    if option == 'A':
        print(user_list or "No users found.")

    elif option == 'B':
        user_list.append(input("New User Name: "))
        print(f"\nCurrent List: {user_list}")

    elif option == 'C':
        old = input("Old User: ")
        if old in user_list:
            user_list[user_list.index(old)] = input("Update User: ")
            print(f"\nCurrent List: {user_list}")
        else:
            print("User not found.")

    elif option == 'D':
        rem = input("Which user to delete: ")
        if rem in user_list:
            user_list.remove(rem)
            print(f"\nCurrent List: {user_list}")
        else:
            print("User not found.")

    elif option == 'E':
        break

    else:
        print("Invalid option. Please Try Again.")

print("\nExiting the system...")



# users_list = []

# while (opt := input("\n===SYSTEM MENU===\n\nA. List users\nB. Add new user\nC. Update a user\nD. Delete a user\nE. Exit\n\nMy choice: ").upper()) != 'E':

#     if opt == 'A':
#         print(users_list or "No users found.")

#     elif opt == 'B':
#         users_list.append(input("New User Name: "))

#     elif opt == 'C':
#         old = input("Old User: ")
#         if old in users_list:
#             users_list[users_list.index(old)] = input("Update User: ")
#         else:
#             print("User not found.")

#     elif opt == 'D':
#         rem = input("Which user to delete: ")
#         if rem in users_list:
#             users_list.remove(rem)
#         else:
#             print("User not found.")

#     else:
#         print("Invalid option.")

#     print("\nCurrent List:", users_list)

# print("\nExiting the system...")


# users_list = []

# while (opt := input ("\n===SYSTEM MENU===\n\nA. List users\nB. Add new user\nC. Update a user\nD. Delete a user\nE. Exit\n\nMy choice: ").upper()) != 'E': 

#     if opt == 'A': print(users_list or "No users found.")

#     elif opt == 'B': users_list.append(input("New User Name: "))
#     elif opt == 'C' and (old := input("Old User: ")) in users_list: users_list[users_list.index(old)] = input("Update User: ")
#     elif opt == 'D' and (rem := input("Which user to delete: ")) in users_list: users_list.remove(rem)
#     print("\nCurrent List: ", users_list)


    
    

