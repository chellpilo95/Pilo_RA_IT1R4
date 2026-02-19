# temp1 = 100
# celsius1 = (temp1 - 32) * 5/9
# print(celsius1)

# temp2 = 88
# celsius2 = (temp2 - 32) * 5/9
# print(celsius2)

# temp3 = 85
# celsius3 = (temp3 - 32) * 5/9
# print(celsius3)

#This part will use a FUNCTION

# def fahrenheit_to_celsius(fahrenheit):
#     return (fahrenheit - 32) * 5/9

# print(fahrenheit_to_celsius(77))
# print(fahrenheit_to_celsius(95))
# print(fahrenheit_to_celsius(50))

#This part will use a FUNCTION with USER INPUT

# def fahrenheit_to_celsius(fahrenheit):
#     return (fahrenheit - 32) * 5/9

# fahrenheit = int(input("Enter the temperature in fahrenheit: "))
# print("The temperature in celsius is", fahrenheit_to_celsius(fahrenheit))

#RETURN STATEMENT

# def multiply(a, b):
#     return a * b

# result = multiply(5, 10)
# print(result)

#DEFAULT ARGUMENTS

# def myFun(x, y=100):
#     print("x: ", x)
#     print("y: ", y)

# myFun(50)

#KEYWORD ARGUMENTS

# def student(lname, fname):
#     print(lname, fname)

# student(fname='Jeonghan', lname='Yoon')
# student(lname='Yoon', fname='Jeonghan')

#POSITIONAL ARGUMENTS

# def nameAge(name, age):
#     print("Hey, I'm", name)
#     print("I'm currently", age)

# print("Case-1:")
# nameAge("jeonghan", 30)

# print("\nCase-2:")
# nameAge(30, "Yoon")

#ARBITRARY ARGUMENTS

# def myFun(*args, **kwargs):
#     print("Non-keyword Arguments (*args):")
#     for arg in args:
#         print(args)

#     print("\nKeyword Arguments (**kwargs):")
#     for key, value in kwargs.items():
#         print(f"{key} == {value}")

# #function call with both types of arguments

# myFun('Hey', 'Welcome', first='Jeonghan', mid='Hannie', last='Yoon')

#PASS STATEMENT

# def get_greeting():
#     pass
# print(get_greeting())

#LOCAL VARIABLE

# def myfunc():
#     x = 500
#     y = 200
#     print(x, y)

# myfunc()

#GLOBAL VARIABLE

x = 500
y = 200

def myfunc():
    print(x, y)

myfunc()