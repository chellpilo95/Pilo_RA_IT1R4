#Assignment: A Basic calculator

Fnum1 = float(input("First number: "))
operation = input("\nOperation (+,-,*,/): ")
Fnum2 = float(input("\nSecond number: "))

if operation == "+": print("\nAnswer:", Fnum1 + Fnum2)
elif operation == "-": print("\nAnswer:", Fnum1 - Fnum2)
elif operation == "*": print("\nAnswer:", Fnum1 * Fnum2)
elif operation == "/": print("\nAnswer:", Fnum1 / Fnum2)