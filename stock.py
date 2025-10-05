 

def stock_tracker():
    
    stock_prices = {
        "AAPL": 180,     
        "GOOGL": 2750.50,   
        "TSLA": 250,     
        "AMZN": 3200.10,   
        "INFY": 1500.25    
    }
 
    portfolio = {
        "AAPL": 5,
        "GOOGL": 2,
        "TSLA": 3,
        "AMZN": 1,
        "INFY": 10
    }

    print("📈 Simple Stock Tracker\n")
    print(f"{'Stock':<10}{'Price':>10}{'Qty':>10}{'Investment':>15}")

    total_investment = 0

    for stock, qty in portfolio.items():
        price = stock_prices.get(stock, 0)
        investment = price * qty
        total_investment += investment
        print(f"{stock:<10}{price:>10.2f}{qty:>10}{investment:>15.2f}")

    print("\n💰 Total Investment: {:.2f}".format(total_investment))
stock_tracker()
