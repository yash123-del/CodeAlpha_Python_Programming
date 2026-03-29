stock_prices = {
    "AAPL": 188,
    "TSLA": 250,
    "GOOG": 135,
    "AMZN": 145,
    "MSFT": 310
}

portfolio = {}
total_investment = 0

print("📊 Stock Portfolio Tracker")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").upper()
    
    if stock == "DONE":
        break
    
    if stock not in stock_prices:
        print("❌ Stock not available.")
        continue
    
    quantity = int(input(f"Enter quantity for {stock}: "))
    
    portfolio[stock] = quantity

print("\n📈 Portfolio Summary:")
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    total_investment += investment
    print(f"{stock} -> {quantity} shares × ${price} = ${investment}")

print(f"\n💰 Total Investment Value: ${total_investment}")

save = input("\nDo you want to save this to a file? (yes/no): ").lower()

if save == "yes":
    file_type = input("Enter file type (txt/csv): ").lower()
    
    if file_type == "txt":
        with open("portfolio.txt", "w") as f:
            f.write("Stock Portfolio Summary\n")
            for stock, quantity in portfolio.items():
                price = stock_prices[stock]
                f.write(f"{stock}: {quantity} shares at ${price}\n")
            f.write(f"\nTotal Investment: ${total_investment}")
        print("✅ Saved as portfolio.txt")
    
    elif file_type == "csv":
        with open("portfolio.csv", "w") as f:
            f.write("Stock,Quantity,Price,Total\n")
            for stock, quantity in portfolio.items():
                price = stock_prices[stock]
                f.write(f"{stock},{quantity},{price},{price * quantity}\n")
            f.write(f"\nTotal,,,{total_investment}")
        print("✅ Saved as portfolio.csv")
    
    else:
        print("❌ Invalid file type.")