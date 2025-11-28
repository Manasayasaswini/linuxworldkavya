while True:
    print("""
    1. hours to minutes
    2. miles to kilometers
    3. kilograms to pounds
    4. degree to radian
    5. celsius to fahrenheit
    6. exit
    """)

    choice = input("enter your choice:")

    if choice == "1":
        hours = input("enter hours:")
        minutes = int(hours) * 60
        print(hours, "hours is", minutes, "minutes")

    elif choice == "2":
        miles = input("enter miles:")
        kilometers = float(miles) * 1.60934
        print(miles, "miles is", kilometers, "kilometers")

    elif choice == "3":
        kg = input("enter kilograms:")
        pounds = float(kg) * 2.20462
        print(kg, "kg is", pounds, "pounds")

    elif choice == "4":
        degree = input("enter degree:")
        radian = float(degree) * 0.0174533
        print(degree, "degree is", radian, "radian")

    elif choice == "5":
        celsius = input("enter celsius:")
        fahrenheit = (float(celsius) * 9/5) + 32
        print(celsius, "celsius is", fahrenheit, "fahrenheit")

    elif choice == "6":
        print("exiting the converter, thank you")
        break

    else:
        print("invalid choice, try again")
