from StockTracker import Transaction
from StockTracker import Position
from StockTracker import Portfolio

def test_transaction():
    # Generric buy
    try:
        test_transaction = Transaction("RDSA", "08/05/2020", "Buy", 100, 1)
        assert test_transaction.name == "RDSA"
        assert test_transaction.date == "08/05/2020"
        assert test_transaction.direction == "buy"
        assert test_transaction.amount == 100
        assert test_transaction.price == 1
        assert test_transaction.currency == "euro"
    except AssertionError:
        print("FAIL: generic buy order")
    else:
        print("PASS: generic buy order")

    # Generic sell
    try:
        test_transaction = Transaction("RDSB", "09/05/2020", "sell", 10, 15.224, "dollar")
        assert test_transaction.name == "RDSB"
        assert test_transaction.date == "09/05/2020"
        assert test_transaction.direction == "sell"
        assert test_transaction.amount == 10
        assert test_transaction.price == 15.224
        assert test_transaction.currency == "dollar"
    except AssertionError:
        print("FAIL: generic sell order")
    else:
        print("PASS: generic sell order")

    # Ivalid direction
    try:
        test_transaction = Transaction("RDSB", "09/05/2020", "hold", 10, 15.224, "dollar")
    except ValueError:
        print("PASS: Bad direction")
    else:
        print("FAIL: Bad direction")

    # Ivalid amount
    try:
        test_transaction = Transaction("RDSB", "09/05/2020", "hold", -1, 15.224, "dollar")
    except ValueError:
        print("PASS: Bad amount")
    else:
        print("FAIL: Bad amount")


def test_position():
    # Test adding sell to new position
    try:
        shell_holdings = Position(Transaction("RDSA", "08/05/2020", "sell", 220, 12.233))
    except ValueError:
        print("PASS: sell before buy")
    else:
        print("FAIL: sell before buy")

    # Add a generic buy:
    try:
        shell_holdings = Position(Transaction("RDSA", "08/05/2020", "buy", 1, 1))
        assert shell_holdings.name == "RDSA"
        assert shell_holdings.value == 1
        assert shell_holdings.amount == 1
        assert shell_holdings.break_even_price == 1
        assert shell_holdings.currency == "euro"
        assert shell_holdings.profit == 0
    except:
        print("FAIL: Add generic buy order")
    else:
        print("PASS: Add generic buy order")

    # Add a generic sell:
    try:
        shell_holdings.add_transaction(Transaction("RDSA", "08/05/2020", "sell", 1, 2))
        assert shell_holdings.name == "RDSA"
        assert shell_holdings.value == 0
        assert shell_holdings.amount == 0
        assert shell_holdings.break_even_price == 0
        assert shell_holdings.currency == "euro"
        assert shell_holdings.profit == 1
    except:
        print("FAIL: Add generic sell order")
    else:
        print("PASS: Add generic sell order")

    # Add a generic sell to closed position:
    try:
        shell_holdings.add_transaction(Transaction("RDSA", "08/05/2020", "sell", 1, 2))
        assert shell_holdings.name == "RDSA"
        assert shell_holdings.value == 0
        assert shell_holdings.amount == 0
        assert shell_holdings.break_even_price == 0
        assert shell_holdings.currency == "euro"
        assert shell_holdings.profit == 1
    except:
        print("PASS: Add sell to closed order")
    else:
        print("FAIL: Add sell to closed order")

    

    # Add a buy and 2 sell:
    try:
        shell_holdings.add_transaction(Transaction("RDSA", "08/05/2020", "buy", 2, 1))
        shell_holdings.add_transaction(Transaction("RDSA", "08/05/2020", "sell", 1, 2))
        shell_holdings.add_transaction(Transaction("RDSA", "08/05/2020", "sell", 1, 2))
        assert shell_holdings.name == "RDSA"
        assert shell_holdings.value == 0
        assert shell_holdings.amount == 0
        assert shell_holdings.break_even_price == 0
        assert shell_holdings.currency == "euro"
        assert shell_holdings.profit == 3
    except:
        print("FAIL: Add generic sell order")
    else:
        print("PASS: Add generic sell order")


    # Add a multiple buys:
    try:
        shell_holdings.add_transaction(Transaction("RDSA", "08/05/2020", "buy", 2, 1))
        shell_holdings.add_transaction(Transaction("RDSA", "08/05/2020", "buy", 1, 3))
        shell_holdings.add_transaction(Transaction("RDSA", "08/05/2020", "buy", 1, 3))
        assert shell_holdings.name == "RDSA"
        assert shell_holdings.value == 8
        assert shell_holdings.amount == 4
        assert shell_holdings.break_even_price == 2
        assert shell_holdings.currency == "euro"
        assert shell_holdings.profit == 3
    except:
        print("FAIL: Add buy series")
    else:
        print("PASS: Add buy series")

    # Add transaction of different product
    try:
        shell_holdings.add_transaction(Transaction("RDSB", "08/05/2020", "buy", 2, 1))
    except:
        print("PASS: add transaction of different product")
    else:
        print("FAIL: add transaction of different product")

    # Add transaction of different currecny
    try:
        shell_holdings.add_transaction(Transaction("RDSB", "08/05/2020", "buy", 2, 1, "dollar"))
    except:
        print("PASS: add transaction of different currecny")
    else:
        print("FAIL: add transaction of different currecny")



def main():
    test_transaction()
    test_position()

if __name__ == '__main__':
    main()