"""
a menu for getting the ops and input numbers:
"""

def menu():
    num1 = float(input("Enter your first number:\n"))
    num2 = float(input("Enter your second number:\n"))
    print('choose one option\n')
    print("""
    1.sum 
    2.difference_numbers 
    3.multiply_numbers
    4.division_numbers
    """)
    op = int(input("select the option's code:"))
    return (num1, num2, op)