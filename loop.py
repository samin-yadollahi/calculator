def loop():
    choice = input("Do you want to continue? (Y,N): ")
    if choice.upper() == "Y":
        calculate()
    elif choice.upper() == "N":
        print("Goodbye!")
    else:
        print("Invalid input!")
        loop()
