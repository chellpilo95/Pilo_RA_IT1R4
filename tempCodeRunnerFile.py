try:
    # Create file safely
    with open("message.txt", "x"):
        print("File created successfully!")

except FileExistsError:
    print("File already exists!")