#Simple Calculator Project in Python
#Author: Quinn

#Creating instance Variables
number1 = 0;
number2 = 0;
result = 0;

#Creating IF Statement/Compareable instance Variables
addition = 'A'
divide = 'D'
multiply = 'M'
power = 'P'
remainder = 'R'
subtraction = "S"
type = "Q"
type2 = "?"
check = False

#Greets User
print("o__________________________o")
print("|Welcome to the Calculator!|")
print("|         By Quinn         |")
print("|__________________________|")

#Informs user of function
print("With this Calulator you are able to Add(A), Subtract(S), Multiply(M) and Divide(D) Power(P) Remainder(R)")
print("--------------------------------------------------------------------------------------------------------\n")

#Assigning Values to variables by getting user input
type = str(input("What type of calculation would you like to do: "))
number1 = int(input("Please insert your First number: "))
number2 = int(input("Please insert your Second number: "))

#This space is to create one gap between the questions and result
print(" ")

#Calculating Based on user input with IF/Else statements
if (type == addition) | (type == (addition.lower())):
    print("Commencing Addition!")
    result = number1 + number2;
    type2 = "+"
    check = True;

elif (type == subtraction) | (type == (subtraction.lower())):
    print("Commencing Subtraction!")
    result = number1 - number2;
    type2 = "-"
    check = True;

elif (type == multiply) | (type == (multiply.lower())):
    print("Commencing Multiplication!")
    result = number1 * number2;
    type2 = "*"
    check = True;

elif (type == divide) | (type == (divide.lower())):
    print("Commencing Division!")
    result = number1 / number2;
    type2 = "/"
    check = True;

elif (type == power) | (type == (power.lower())):
    print("Calculating the Power!")
    result = number1 ** number2;
    type2 = "^"
    check = True;

elif (type == remainder) | (type == (remainder.lower())):
    print("Calculating the Remainder!")
    result = number1 % number2;
    type2 = "%"
    check = True;

#Creates response if input is invalid
else:
    print("Invalid Input! Please make it [A, S, D, M, P, R] to be valid")

#Output back to user with results of calculation
if (check == True):
    print(number1, type2, number2, "=", result)
