# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 170,
    "MSFT": 320
}

print("=== Stock Portfolio Tracker ===")

total_investment = 0
portfolio = {}

# Input number of stocks
n = int(input("How many different stocks you want to add? "))

for i in range(n):
    stock = input("Enter stock name (AAPL/TSLA/GOOG/AMZN/MSFT): ").upper()
    quantity = int(input("Enter quantity: "))

    if stock in stock_prices:
        value = stock_prices[stock] * quantity
        portfolio[stock] = value
        total_investment += value
    else:
        print("Invalid stock name!")

print("\n--- Portfolio Summary ---")
for stock, value in portfolio.items():
    print(f"{stock}: ₹{value}")

print(f"\nTotal Investment Value: ₹{total_investment}")

# Optional: Save to file
save = input("\nDo you want to save result? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        for stock, value in portfolio.items():
            file.write(f"{stock}: ₹{value}\n")
        file.write(f"\nTotal Investment: ₹{total_investment}\n")

    print("Saved to portfolio.txt")