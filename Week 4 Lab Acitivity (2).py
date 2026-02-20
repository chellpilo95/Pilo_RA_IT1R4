#Find the largest number among three numbers entered by the user

def checking(A, B, C):

    if A == B and A == C:
        print(f"{A}, {B}, and {C} are all equal number\n")

    elif A > B and A > C:
        print(f"\nThe first number is the largest number with a value of {A}\n")

    elif B > A and B > C:
        print(f"\nThe second number is the largest number with a value of {B}\n")

    elif C > A and C > B:
        print(f"\nThe third number is the largest number with a value of {C}\n")

A = int(input("Enter your first number: "))
B = int(input("\nEnter your second number: "))
C = int(input("\nEnter your third number: "))

checking (A, B, C)


