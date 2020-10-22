from StockTracker import Transaction
from StockTracker import Position
from StockTracker import Portfolio

def test_transaction():
    # Generric buy
    try:
        test_transaction = Transaction("RDSA", "08/05/2020", "Buy", 100, 1, "EAM")
        assert test_transaction.name == "RDSA"
        assert test_transaction.date == "08/05/2020"
        assert test_transaction.direction == "buy"
        assert test_transaction.amount == 100
        assert test_transaction.price == 1
        assert test_transaction.index == "EAM"
        assert test_transaction.currency == "EUR"
    except AssertionError:
        print("FAIL: generic buy order")
    else:
        print("PASS: generic buy order")

    # Generic sell
    try:
        test_transaction = Transaction("RDSB", "09/05/2020", "sell", 100, 15.224, "EAM", "USD")
        assert test_transaction.name == "RDSB"
        assert test_transaction.date == "09/05/2020"
        assert test_transaction.direction == "sell"
        assert test_transaction.amount == 10
        assert test_transaction.price == 15.224
        assert test_transaction.index == "EAM"
        assert test_transaction.currency == "USD"
    except AssertionError:
        print("FAIL: generic sell order")
    else:
        print("PASS: generic sell order")

    # Ivalid direction
    try:
        test_transaction = Transaction("RDSB", "09/05/2020", "hold", 10, 15.224, "EAM", "USD")
    except ValueError:
        print("PASS: Bad direction")
    else:
        print("FAIL: Bad direction")

    # Ivalid amount
    try:
        test_transaction = Transaction("RDSB", "09/05/2020", "hold", -1, 15.224, "EAM", "USD")
    except ValueError:
        print("PASS: Bad amount")
    else:
        print("FAIL: Bad amount")

    
    # Ivalid index
    try:
        test_transaction = Transaction("RDSB", "09/05/2020", "hold", -1, 15.224, 4)
    except ValueError:
        print("PASS: Bad index")
    else:
        print("FAIL: Bad index")

    # Ivalid index
    try:
        test_transaction = Transaction("RDSB", "09/05/2020", "hold", -1, 15.224, "EAM", "pounds")
    except ValueError:
        print("PASS: Bad index")
    else:
        print("FAIL: Bad index")


def test_position():
    # Test adding sell to new position
    try:
        shell_holdings = Position(Transaction("RDSA", "08/05/2020", "sell", 220, 12.233, "EAM"))
    except ValueError:
        print("PASS: sell before buy")
    else:
        print("FAIL: sell before buy")

    # Add a generic buy:
    try:
        shell_holdings = Position(Transaction("RDSA", "01/05/2020", "buy", 1, 1, "EAM"))
        assert shell_holdings.name == "RDSA"
        assert shell_holdings.value == 1
        assert shell_holdings.amount == 1
        assert shell_holdings.break_even_price == 1
        assert shell_holdings.currency == "EUR"
        assert shell_holdings.profit == 0
    except:
        print("FAIL: Add generic buy order")
    else:
        print("PASS: Add generic buy order")

    # Add a generic sell:
    try:
        shell_holdings.add_transaction(Transaction("RDSA", "02/05/2020", "sell", 1, 8, "EAM"))
        assert shell_holdings.name == "RDSA"
        assert shell_holdings.value == 0
        assert shell_holdings.amount == 0
        assert shell_holdings.break_even_price == 0
        assert shell_holdings.currency == "EUR"
        assert shell_holdings.profit == 7
    except:
        print("FAIL: Add generic sell order")
    else:
        print("PASS: Add generic sell order")

    print(shell_holdings)

    # Add a generic sell to closed position:
    try:
        shell_holdings.add_transaction(Transaction("RDSA", "02/05/2020", "sell", 1, 2, "EAM"))
    except:
        print("PASS: Add sell to closed order")
    else:
        print("FAIL: Add sell to closed order")

    

    # Add a buy and 2 sell:
    try:
        shell_holdings.add_transaction(Transaction("RDSA", "03/05/2020", "buy", 2, 1, "EAM"))
        shell_holdings.add_transaction(Transaction("RDSA", "04/05/2020", "sell", 1, 2, "EAM"))
        shell_holdings.add_transaction(Transaction("RDSA", "05/05/2020", "sell", 1, 2, "EAM"))
        assert shell_holdings.name == "RDSA"
        assert shell_holdings.value == 0
        assert shell_holdings.amount == 0
        assert shell_holdings.break_even_price == 0
        assert shell_holdings.currency == "EUR"
        assert shell_holdings.profit == 9
    except:
        print("FAIL: Add buy and sell")
    else:
        print("PASS: Add buy and sell")


    # Add a multiple buys:
    try:
        shell_holdings.add_transaction(Transaction("RDSA", "08/05/2020", "buy", 2, 1, "EAM"))
        shell_holdings.add_transaction(Transaction("RDSA", "08/05/2020", "buy", 1, 3, "EAM"))
        shell_holdings.add_transaction(Transaction("RDSA", "08/05/2020", "buy", 1, 3, "EAM"))
        assert shell_holdings.name == "RDSA"
        assert shell_holdings.value == 8
        assert shell_holdings.amount == 4
        assert shell_holdings.break_even_price == 2
        assert shell_holdings.currency == "EUR"
        assert shell_holdings.profit == 9
    except:
        print("FAIL: Add buy series")
    else:
        print("PASS: Add buy series")

    # Add transaction of different product
    try:
        shell_holdings.add_transaction(Transaction("RDSB", "08/05/2020", "buy", 2, 1, "EAM"))
    except:
        print("PASS: add transaction of different product")
    else:
        print("FAIL: add transaction of different product")

    # Add transaction of different currecny
    try:
        shell_holdings.add_transaction(Transaction("RDSA", "08/05/2020", "buy", 2, 1, "EAM", "USD"))
    except:
        print("PASS: add transaction of different currecny")
    else:
        print("FAIL: add transaction of different currecny")

    # Add transaction of different currecny
    try:
        shell_holdings.add_transaction(Transaction("RDSA", "08/05/2020", "buy", 2, 1, "EAS"))
    except:
        print("PASS: add transaction of different index")
    else:
        print("FAIL: add transaction of different index")

    print(shell_holdings)
    #.generate_tax_events()

def test_portfolio():
    new_portfolio = Portfolio()
    new_portfolio.add_transaction(Transaction("RDSA", "08/05/2020", "buy", 3, 1, "EAM", "USD"))
    new_portfolio.add_transaction(Transaction("RDSA", "08/05/2020", "buy", 2, 2, "EAM", "USD"))
    new_portfolio.add_transaction(Transaction("RDSA", "08/05/2020", "sell", 4, 3, "EAM", "USD"))
    new_portfolio.add_transaction(Transaction("RDSB", "08/05/2020", "buy", 1, 3, "EAM", "USD"))
    new_portfolio.add_transaction(Transaction("RDSB", "08/05/2020", "buy", 1, 3, "EAM", "USD"))
    new_portfolio.add_transaction(Transaction("RDSB", "08/05/2020", "sell", 2, 1, "EAM", "USD"))
    new_portfolio.print_positions()

    csv_portfolio = Portfolio('Transactions.csv', 'degiro')
    csv_portfolio.print_positions()

def test_csv_reader():
    csv_file = "./Transactions.csv"
    new_portfolio = Portfolio()
    new_portfolio.add_from_csv(csv_file)

def main():
    #test_transaction()
    #test_position()
    test_portfolio()
    #test_csv_reader()

if __name__ == '__main__':
    main()