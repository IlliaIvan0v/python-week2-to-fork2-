print("Welcome to the Currency Converter 228! \n")


def Converterfunction():
    while True:
        try:
            amount_of_money = float(input("Enter the\
 amount of money. (Dollars): "))
        except ValueError:
            print("\nError! You need to enter a number. Try again.")
            continue
        print("\nChoose the target currency for conversion!\
\n1. Euro\n2. Pound\n3. Yen")
        currency = input("\nChoose the currency (enter the number): ")
        if currency == "1":
            resultEuro = amount_of_money * 0.91
            print("\nConversion Result:")
            print(f"{amount_of_money:.2f} dollars are equel\
 to {resultEuro:.2f} euros.")
        elif currency == "2":
            resultPound = amount_of_money * 0.78
            print("Conversion Result:")
            print(f"{amount_of_money:.2f} dollars are equel\
 to {resultPound:.2f} pounds.")
        elif currency == "3":
            resultYen = amount_of_money * 140.88
            print("Conversion Result:")
            print(f"{amount_of_money:.2f} dollars are equel\
 to {resultYen:.2f} Yens.")
        answer = input("\nDo you want to perform another\
conversion? (Yes/No): ")
        if answer == "No":
            print("\nThank you for using the Currency Converter 228. Goodbye!")
            break
        elif answer == "Yes":
            continue
        else:
            print("\nError! You need to enter a Yes or No. Try again.")


Converterfunction()
