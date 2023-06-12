from menu import menu
from calculate import Calculation

def check_menu():

    num1, num2, op = menu(num1, num2, op)

    if (op == 1):
        print (Calculation.sum_numbers(num1, num2))
    
    elif(op == 2):
        print (Calculation.difference_numbers(num1, num2))

    elif(op == 3):
        print (Calculation.multiply_numbers(num1, num2))

    elif(op == 4):
        print (Calculation.division_numbers(num1, num2))
