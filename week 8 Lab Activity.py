try:
    # Create file safely
    with open("message.txt", "x"):
        print("File created successfully!")

except FileExistsError:
    print("File already exists!")

while True:
    print("\nWelcome to Messaging App!\n")
    print("1. Send Message")
    print("2. View Messages")
    print("3. Exit")
    
    choice = input("\nEnter your choice: ")
    
    if choice == '1':
        message = input("\nEnter your message: ")
        
        # Prevent empty messages
        if message.strip():
            try:
                with open("message.txt", "a") as f:
                    f.write(message + "\n")
                print("\nMessage sent successfully!")

            except Exception as e:
                print("\nError Sending the Message:", e)
        else:
            print("Message cannot be empty.")
    
    elif choice == '2':
        try:
            with open("message.txt", "r") as f:
                messages = f.readlines()
                
                if messages:
                    print("\n--- Messages ---\n")
                    for msg in messages:
                        print(msg.strip())
                else:
                    print("No messages found.")

        except Exception as e:
            print("Error reading the message:", e)
    
    elif choice == '3':
        print("Exiting the program....")
        break
    
    else:
        print("Invalid choice. Please enter again.")




# try:
#     f = open("message.txt", "x")
#     print("File created successfully!")
#     f.close()

# except FileExistsError:
#     print("File already exists!")

# while True:
#     print("\nWelcome to Messaging App!\n")
#     print("1. Send Message")
#     print("2. View Messages")
#     print("3. Exit")
    
#     choice = input("\nEnter your choice: ")
    
#     if choice == '1':
#         message = input("\nEnter your message: ")
#         try:
#             with open("message.txt", "a") as f:
#                 f.write(message + "\n")
#             print("\nMessage sent successfully!")

#         except Exception as e:
#             print("\nError Sending the Message: ")
    
#     elif choice == '2':
#         try:
#             with open("message.txt", "r") as f:
#                 messages = f.readlines()
#                 if messages:
#                     print("\n--- Messages ---\n")
#                     for msg in messages:
#                         print(msg.strip())
#                 else:
#                     print("No messages found.")

#         except Exception as e:
#             print("Error reading the message: ")
    
#     elif choice == '3':
#         print("Exiting the program....")
#         break
    
#     else:
#         print("Invalid choice. Please enter again.")

