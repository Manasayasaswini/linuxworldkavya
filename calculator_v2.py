#CALCULATOR PROGRAM

print("\nCALCULATOR\n")
print("List of operators:", "Add:+ ", "Substract:- ", "Multiplication:* ", "Division:/ ", "Remainder:% ", "Power:**  \n") 
num1 = int(input("Enter your first number: "))
output1 = num1
operator = input("Enter the operator: ")
num2 = int(input("Enter your second number: "))

def calculator (num1, num2):
    if (operator != '+' and operator != '-' and operator != '*' and operator != '/' and operator != '%' and operator != '**'):
        print("Enter a valid operator\n")
        num1 = output1
        return num1
    if (operator == '+'):
        print(f"{num1} + {num2} = {num1 + num2}\n")
        return num1 + num2
    if (operator == '-'):
        print(f"{num1} - {num2} = {num1 - num2}\n")
        return num1 - num2
    if (operator == '*'):
        print(f"{num1} x {num2} = {num1 * num2}\n")
        return num1 * num2
    if (operator == '/'):
        if (num2 == 0):
            print(f"{num1} cannot be divided with {num2}.\n")
            num1 = output1
            return num1
        print(f"{num1} / {num2} = {num1 / num2}\n")
        return num1 / num2
    if (operator == '%'):
        if (num2 == 0):
            print(f"{num1} cannot be divided with {num2}.\n")
            num1 = output1
            return num1
        print(f"Remainder: {num1} % {num2} = {num1 % num2}\n")
        return num1 % num2
    if (operator == '**'):
        print(f"{num1} power {num2} = {num1 ** num2}\n")
        return num1 ** num2

output1 = calculator (num1, num2)

def result_func ():
    new_result = input("To exit enter 'q'. To continue enter 'c'. your response: ")
    return new_result

result = result_func()

while (result == 'c'):
    if (result == 'q' and result != 'c'):
        break
    print(f"\nThe first number is the previous result: {output1}")
    num1 = output1
    operator = input("Enter the operator: ")
    num2 = int(input("Enter your second number: "))
    output1 = calculator (num1, num2)
    result = result_func()
