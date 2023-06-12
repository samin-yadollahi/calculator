def calculate():
    a, b, op = prompt_menu()
    if op == 1:
        print("Sum: {} + {} = {}".format(a,b,a+b))
    elif op == 2:
        print("Difference: {} - {} = {}".format(a,b,a-b))
    elif op == 3:
        print("Product: {} * {} = {}".format(a,b,a*b))
    elif op == 4:
        print("Power: {}^{} = {}".format(a,b,a**b))
    elif op == 5:
        try:
            print("Quotient: {} / {} = {}".format(a,b,a/b))
        except:
            print("Division by 0 not possible!")
    elif op == 6:
        try:
            print("Division with remainder: {} / {} = {} Remainder: {}".format(a,b,a//b,a%b))
        except:
            print("Divsion by 0 not possible!")
    else:
        print("No such choice!")
    loop()
