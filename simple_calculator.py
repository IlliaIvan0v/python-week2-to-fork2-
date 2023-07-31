print("Hello! Welocome to the simple calculator 3000 pro Maxrosoft!")


def simpleCalculator():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Error! You need to enter a number")
            continue

        print(
            "\nMenu:\n 1. Addition\n 2.\
 Subtraction\n 3. Multiplication\n 4. Division\n"
        )
        operation = str(input("Enter your operation (enter the number): "))
        if operation == "1":
            print("Result:", int(num1) + int(num2))
        elif operation == "2":
            print("Result:", int(num1) - int(num2))
        elif operation == "3":
            print("Result:", int(num1) * int(num2))
        elif operation == "4":
            print("Result:", round(int(num1) / int(num2), 2))
        answer = input("Do you want to continue? (Yes/No): ")
        if answer == "No":
            print("Thank you for using the simple calculator 3000 Maxrosoft")
            break
        else:
            print("\nError! You need to enter a Yes or No. Try again.")


simpleCalculator()
