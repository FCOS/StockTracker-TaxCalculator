from . import Transaction
from . import Position
import os

class Portfolio:
    def __init__(self, csv_file=None, csv_format='degiro'):
        self.value = 0
        self.num_open_positions = 0
        self.num_closed_positions = 0
        self.positions = {}
        if csv_file != None:
            self.add_from_csv(csv_file, csv_format)
        
    def __str__(self):
        pass

    def print_positions(self):
        for key in self.positions.keys():
            print(self.positions[key])

    def add_transaction(self, transaction):
        ID = transaction.name + transaction.index
        if ID in self.positions:
            self.value -= self.positions[ID].value
            position = self.positions[ID]
            position += transaction
            self.value += self.positions[ID].value

            if self.positions[ID].amount == 0:
                # Position is now closed
                self.num_closed_positions += 1
                self.num_open_positions -= 1
            elif self.positions[ID].amount == transaction.amount:
                # Position has been reopened
                self.num_closed_positions -= 1
                self.num_open_positions += 1
        else:
            self.positions[ID] = Position(transaction)
            #New position, thus must be a buy
            self.num_open_positions += 1
            self.value += transaction.price * transaction.amount

        

    def add_from_csv(self, csv_file, csv_format='degiro'):
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
                self.add_transaction(transaction)
                line = csv.readline()
