balance = 5000
pin = 1234
password = "kavya"
attempts = 0
max_attempts = 3

while True:

    while attempts < max_attempts:
        user_pin = int(input("Enter your PIN: "))
        user_password = input("Enter your password: ")

        if user_pin == pin and user_password == password:

            print("Your balance is", balance)
            amount = int(input("Enter amount to withdraw: "))
            amount2 = int(input("Enter amount to deposit: "))

            # Withdrawal
            if amount <= balance:
                balance -= amount
                print("Amount withdrawn successfully! New balance is:", balance)
            else:
                print("Insufficient balance for withdrawal.")
                break

            # Deposit
            balance += amount2
            print("Amount deposited successfully! New balance is:", balance)

        else:
            attempts += 1
            print(f"Incorrect PIN or password! Attempts left: {max_attempts - attempts}")

    if attempts == max_attempts:
        print("Access blocked due to 3 incorrect attempts.")
        break
