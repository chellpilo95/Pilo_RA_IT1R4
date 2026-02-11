while True:
    password = input ("\nEnter Password: ")

    has_letter = False
    has_number = False

    for char in password:
        if char.isalpha():
            has_letter = True
        
        if char.isdigit():
            has_number = True
    
    if has_letter and has_number:
        print("\n------------------------------")
        print("      Password Accepted.")
        print("------------------------------")
        break

    else:
        print("\n------------------------------")
        print("Invalid Password. Try Again.")
        print("------------------------------")
