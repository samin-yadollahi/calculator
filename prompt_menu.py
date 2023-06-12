def prompt_menu():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    print("""
        Choose an operation from the list:
        1. Addition
        2. Subtraction
        3. Multiplication
        4. Exponentiation
        5. Division
        6. Division with remainder
        """)
    op = int(input("Enter the choice number: "))
    return a, b, op