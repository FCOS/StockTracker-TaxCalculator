from . import Transaction

class Portfolio:
    def __init__(self):
        self.temp = ""

    def add_transaction(self, transaction):
        pass

    def parse_csv(self, csv_file, csv_format='degiro'):
        with open(csv_file, 'r') as csv:
            # Disacrd header
            line = csv.readline()
            line = csv.readline()
            while line != "":
                if csv_format=="degiro":
                    date, _, name, _, index, amount, currency, price, *_  = line.split(',')
                amount = int(amount)
                price = float(price)
                if amount < 0:
                    direction = 'sell'
                    amount = abs(amount)
                else:
                    direction = "buy"
                transaction = Transaction(name, date, direction, amount, price, index, currency)
                print(transaction)
                line = csv.readline()
