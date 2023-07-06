import os

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b


operation_dict={
       "+":add,
       "-":subtract,
       "*":multiply,
       "/":divide
}


def calculator():
    number1=float(input("Enter First Number:"))

    for symbol in operation_dict:
        print(symbol)

    continue_flag=True

    while continue_flag:

        op_symbol=input("Pick an Operation:")

        number2=float(input("Enter Second Number:"))

        calculator_function=operation_dict[op_symbol] #add

        output=calculator_function(number1,number2)

        print(f"{number1} {op_symbol} {number2} = {output}")

        should_continue=input(f"Enter 'Y' to continue calculation with {output} or 'N' to start a new calculator or 'x' to exit.").lower()

        if should_continue == 'y':

            number1=output

        elif should_continue == 'n':
             continue_flag=False

             os.system('cls')

             calculator()

        else:

             continue_flag=False

             print("Thanks For Using Our Program, Wish You Best Of Luck ✌️.")


calculator()





