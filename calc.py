"""
This Program does a simple calculation
"""

def calculate():
    first_input = int(input("Enter first number "))
    operator_input = input("Enter operator ")
    second_input = int(input("Enter Second number "))
    operators = ['+', '-', '/', '*']
    for sign in operators:
        if operator_input == sign :
            print(first_input + second_input )
        elif operator_input == sign:
            print(first_input - second_input ) 
        elif operator_input == sign:
            print (first_input / second_input)
        elif operator_input == sign:
            print(first_input * second_input)

calculate()