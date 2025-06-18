import math  #Import for Mathematics library

#Definition of operation functions

# Two-number operation :
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0 :
        return " Error : Undefined "
    return a / b

def mod(a, b):
    return a % b

def exponent(a, b):
    return a ** b

# One-number operations :
def sine(a):
    # Convert degrees to radians before using Sine
    return math.sin(math.radians(a))

def cosine(a):
    #  Convert degrees to radians before using Cosine
    return math.cos(math.radians(a))

def tangent(a):
    #  Convert degrees to radians before using Tangent
    return math.tan(math.radians(a))

def square_root(a):
    if a <= 0:
        return "Error : Positive integers only"
    return math.sqrt(a)

def log(a):
    if a <= 0 :
        return " Error : undefined for zero and negative numbers"
    return math.log10(a)

def natural_log(a):
    if a <= 0 :
        return " Error : Cant natural log to zero"
    return math.log(a)

def factorial(a):
    # Check if the input is a non-negative integer
    if not a.is_integer() or a < 0 :
        return " Error : Positive integers only"
    return math.factorial(int(a))

def absolute(a):
    return math.fabs(a)


# Main Program Loop
while True :
    print("\nAdvanced Calculator\n")
    print("Choose an operation : ")
    print("1. Addition(+)")
    print("2. Subtraction(-)")
    print("3. Multiplication(*)")
    print("4. Division(/)")
    print("5. Modulus(%)")
    print("6. Exponent(^)")
    print("7. Square root(sqrt)")
    print("8. Log(base 10)")
    print("9. Natural log(In)")
    print("10. Factorial(!)")
    print("11. Absolute(|x|)")
    print("12. Sin()")
    print("13. Cos()")
    print("14. Tan()")
    print("Q. Quit")

    # Get user's choice
    choice = input("\nEnter Choice : ").strip().upper()

    # Exit condition
    if choice == 'Q':
        print("Calculator Closed")
        break

    # Validate input choice
    if choice not in [str(i) for i in range(1, 15)]:
        print(" Error : Invalid Choice")
        continue

    #For two-number operations
    if choice in ['1', '2', '3', '4', '5', '6']:
       try:
           num1 = float(input(" 1st Number : "))
           num2 = float(input(" 2nd Number : "))
       except ValueError:
              print("Error : Invalid Entry")
              continue

       #Perform the selected operation
       if choice == '1' :
          result = add(num1, num2)
          operation = '+'

       elif choice == '2' :
           result = sub(num1, num2)
           operation = '-'

       elif choice == '3' :
            result = mul(num1, num2)
            operation = '*'

       elif choice == '4' :
             result = div(num1, num2)
             operation = '/'

       elif choice == '5' :
             result = mod(num1, num2)
             operation = '%'

       elif choice == '6' :
             result = exponent(num1, num2)
             operation = '^'

       # Display the result
       print(f" Ans : {num1} {operation} {num2} = {result}")

    #For one-number operation
    else :
        try:
            num = float(input("Enter Number : "))
        except ValueError:
            print("Error : Invalid Entry")

        # Perform the selected operation
        if choice == '7':
            result = square_root(num)

        elif choice == '8':
            result = log(num)

        elif choice == '9':
            result = natural_log(num)

        elif choice == '10':
            result = factorial(num)

        elif choice == '11' :
            result = absolute(num)

        elif choice == '12':
            result = sine(num)

        elif choice == '13':
            result = cosine(num)

        elif choice == '14':
            result = tangent(num)

        #Display of result
        print(f" Ans : {round(result, 10)}") #This rounds the result to 10 decimal places




