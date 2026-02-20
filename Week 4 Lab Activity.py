x = 300

def closest(A, B, C):

    diffA = abs(x - A); diffB = abs(x - B); diffC = abs(x - C)

    if A == B and B == C:
        print(f"A is {A}, B is {B}, C is {C}, hence, all numbers are equal.")

    elif diffA < diffB and diffA < diffC:
        print(f"\nThe closest number to {x} is the first number with a value of {A}")

    elif diffB < diffA and diffB < diffC:
        print(f"\nThe closest number to {x} is the second number with a value of {B}")

    elif diffC < diffA and diffC < diffB:
        print(f"\nThe closest number to {x} is the third number with a value of {C}")

    else:
        print(f"\nTwo numbers are equally closest to {x}")


A = int(input("Enter first number: "))
B = int(input("\nEnter second number: "))
C = int(input("\nEnter third number: "))

closest(A, B, C)