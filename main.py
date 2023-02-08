currency = int(input("Please enter a numerical amount of money: "))
currencyTYPE = int(input(
    "Please pick the currency type: dollars (1), pounds(2), rubles(3), or euros(4): "))

if currencyTYPE == 1:
    currency = currency
    print(f"Amount in dollars: {currency}")

elif currencyTYPE == 2:
    currency *= 0.83
    print(f"Amount in pounds: {currency}")

elif currencyTYPE == 3:
    currency *= 73.12
    print(f"Amount in rubles: {currency}")

elif currencyTYPE == 4:
    currency *= 0.93
    print(f"Amount in euros: {currency}")

else:
    currencyTYPE = int(input(
        "Please pick the currency type: dollars (1), pounds(2), rubles(3), or euros(4): "))
