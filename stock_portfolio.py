

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 150
}

total_investment = 0

print("=" * 45)
print("      STOCK PORTFOLIO TRACKER")
print("=" * 45)

while True:
    stock = input("\nEnter Stock Name (AAPL, TSLA, GOOGL, MSFT, AMZN): ").upper()

    if stock not in stock_prices:
        print(" Stock not available.")
        continue

    try:
        quantity = int(input("Enter Quantity: "))

        if quantity <= 0:
            print("Quantity should be greater than 0.")
            continue

    except ValueError:
        print("Please enter a valid number.")
        continue

    investment = stock_prices[stock] * quantity
    total_investment += investment

    print(f" {stock} Investment = ${investment}")

    choice = input("\nDo you want to add another stock? (yes/no): ").lower()

    if choice != "yes":
        break

print("\n" + "=" * 45)
print(f" Total Investment = ${total_investment}")
print("=" * 45)

with open("investment_summary.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    file.write("----------------------------\n")
    file.write(f"Total Investment = ${total_investment}")

print("\nInvestment summary saved in investment_summary.txt")
print("Thank You!")
