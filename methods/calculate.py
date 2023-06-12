"""
this class is going to comput 2 digits, and included for oprations such as summation,
defference, multiply and division
"""

class Calculation:
    def sum_numbers( num1, num2, result):
       result = num1 + num2
       return (result)


    def difference_numbers( num1, num2, result):
        result = num1 - num2
        return (result)


    def multiply_numbers( num1, num2, result):
        result = num1 * num2
        return (result)

    
    def division_numbers( num1, num2, result):
        if (num2 != 0):
            result = num1 / num2
            return (result)

        else:
            return ("zero division error")
        
    