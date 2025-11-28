while True:
    try:
        print("""
        1. addition
        2. subtraction
        3. multiplication
        4. division
        5. modulus
        6. square_root
        7. exit
        """)

        choice = input("Enter your choice: ")

        if choice == "1":
            num1 = int(input("Enter number 1: "))
            num2 = int(input("Enter number 2: "))
            print("Addition is:", num1 + num2)

        elif choice == "2":
            num1 = int(input("Enter number 1: "))
            num2 = int(input("Enter number 2: "))
            print("Subtraction is:", num1 - num2)

        elif choice == "3":
            num1 = int(input("Enter number 1: "))
            num2 = int(input("Enter number 2: "))
            print("Multiplication is:", num1 * num2)

        elif choice == "4":
            num1 = int(input("Enter number 1: "))
            num2 = int(input("Enter number 2: "))
            if num2 != 0:
                print("Division is:", num1 / num2)
            else:
                print("Cannot divide by zero.")

        elif choice == "5":
            num1 = int(input("Enter number 1: "))
            num2 = int(input("Enter number 2: "))
            print("Modulus is:", num1 % num2)

        elif choice == "6":
            num1 = int(input("Enter number 1: "))
            if num1 >= 0:
                print("Square root value is:", num1 ** 0.5)
            else:
                print("Don't enter negative numbers.")

        elif choice == "7":
            print("Exiting the calculator, thank you!")
            break

        else:
            print("Invalid choice, try again.")

    except:
        print("Invalid input! Please enter numbers only.")
