# menu of calculator
print("-------Calculator--------")

# addition fuinction
def addition():
    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))
    num3 = num1 + num2
    print("the sum of num1 & num2 is:", num3)


# Subtraction function 
def subtraction():
    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))
    num3 = num1 - num2
    print("the subtraction of num1 & num2 is:", num3)

# multiplication function
def multiplication():
    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))
    num3 = num1 * num2
    print("the multiplication of num1 & num2 is:", num3)

# division funtion
def division():
    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))
    num3 = num1 / num2
    print("the division of num1 & num2 is:", num3)

# logic loop for running calculations again or finish operations
while True:
    print("---Add = 1 | Subtract = 2 | Multiply = 3 | Divide = 4 | Exit = 0---")
    Operation = int(input("Choose the operation to perform: "))
    if Operation == 1:
        addition()
    elif Operation == 2:
        subtraction()
    elif Operation == 3:
        multiplication()
    elif Operation == 4:
        division()
    elif Operation == 0:
        print("Goodbye!")
        break
    else:
        print("Invalid Operation!")
