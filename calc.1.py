# Basic Arithmetic Calculator 

#Definition of functions
def add(a, b): #addition function
    return a + b
def sub(a, b): #subtraction function
    return a - b
def mult(a, b): #multiplication function
    return a * b
def div(a, b): #division function
    if (b == 0):
        return " Undefined : cannot divide by 0"
    return a / b

#Loop for calculator 
while True :
    print("\nChoose an operation:")
    print("Enter '1' for ADDITION(+)")
    print("Enter '2' for SUBTRACTION(-)")
    print("Enter '3' for Multiplication(*)")
    print("Enter '4' for DIVISION(/)")
    print("Enter 'e' to exit")

# show operations options for user to choose their operation for their calculations
    choice =input("\nEnter choice:").strip().lower()

    if (choice == 'e'):
        print("Calculator Closed, Good Bye. ")
        break #Discontinue using the calculator by exiting loop(Exit)

#Check if the choice is valid
    if (choice not in ['1', '2', '3', '4']):
        print("Invalid Entry, Retry:")
        continue #Start from the beginning

#Prompt for User's Entry of numbers and resulting output for invalid enteries
    try:
        num1 = float(input("Enter First Number :")) #converts input to float
        num2 = float(input("Enter Second Number :")) #converts input to float
    except ValueError : # Output result of error
        print("Invalid Entry, please try again")
        continue #start from beginning

#Calculation(Using the initially stated functions) and selection of symbols to be used in final results display
    if (choice == '1'):
        result = add(num1, num2)
        operation = "+"

    elif (choice == '2'):
        result = sub(num1, num2)
        operation = "-"

    elif (choice == '3'):
        result = mult(num1, num2)
        operation = '*'

    elif (choice == '4'):
        result = div(num1, num2)
        operation = '/'

#Display of final results
    print(f"Final Results :\n {num1} {operation} {num2} = {result} ")
    continue







