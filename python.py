from math import *
num1 = float(input("please input the first number: "))
num2 = float(input("please input the second number: "))
symbol = input("please input the symbol you'd like to use: ")

if symbol == "plus" or symbol == "+":
    print(num1 + num2)
elif symbol == "multiply" or symbol == "*" or symbol == "x":
    print(num1 * num2)
elif symbol == "divide" or symbol == "/":
    print(num1 / num2)
elif symbol == "minus" or symbol == "-":
    print(num1 - num2)
else:
    print("invalid operator, try again")
