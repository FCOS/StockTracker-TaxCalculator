from collections import deque  
import logging

class Position:
    def __init__(self, transaction):
        logging.debug('Creating new position')
        self.validate_args(transaction)

        self.name = transaction.name
        self.value = transaction.amount * transaction.price
        self.amount = transaction.amount
        self.break_even_price = transaction.price
        self.currency = transaction.currency
        self.profit = 0
        self.transactions = deque()
        logging.debug('Adding initial transaction:')
        logging.debug(transaction)
        self.transactions.append(transaction)

    def __str__(self):
        return_str = self.name + ", "
        return_str += "Quantity: " + str(self.amount) + ", "
        return_str += "Value: " + str(self.value) + ", "
        return_str += "BEP: " + str(self.break_even_price) + ", "
        return_str += "Closed profit: " + str(self.profit) + ", "
        
        return return_str 

    def print(self):
        for transaction in self.transactions:
            print(transaction)

    def add_transaction(self, transaction):
        logging.debug('Adding new transaction to position:')
        logging.debug(transaction)
        self.validate_transaction(transaction)

        # Sales get resolvedd imediately
        if transaction.direction == "sell":
            # Keep track of the purchasing cost of the transactions we are closing for profit and tax
            purchase_cost = 0
            for old_transaction in self.transactions:
                if old_transaction.direction == "sell":
                    continue
                else:
                    if old_transaction.open <= transaction.open:
                        # If we can close entire order, do so
                        # Update total cost of shares we are closing
                        purchase_cost += old_transaction.price * old_transaction.open
                        # remove the open sell orders
                        transaction.open -= old_transaction.open
                        # remove the open buy orders
                        old_transaction.open = 0
                    else:
                        # We cannot close entire order, close what we can, and finish
                        purchase_cost += old_transaction.price * transaction.open
                        # Close fulfilled buys on old order
                        old_transaction.open -= transaction.open
                        transaction.open = 0
                    if transaction.open == 0:
                        break
            transaction.profit = (transaction.price * transaction.amount) - purchase_cost
        
        self.transactions.append(transaction)

        self.update_position()


    def update_position(self):
        self.value = 0
        self.amount = 0
        self.break_even_price = 0
        self.profit = 0

        #logging.debug('Updating position')
        for transaction in self.transactions:
            if transaction.direction == "buy":
                self.value += transaction.price * transaction.open
                self.amount += transaction.open
                self.break_even_price += transaction.price * transaction.open
            else:
                self.profit += transaction.profit
        
        if self.amount != 0:
            self.break_even_price /= self.amount


    def generate_tax_events(self):
        pass

    def validate_transaction(self, transaction):
        #Validate name
        if self.name != transaction.name:
            raise ValueError("Transaction with name " + transaction.name + " cannot be added to Position of " + self.name)
        
        #Validate currency
        if self.currency != transaction.currency:
            raise ValueError("Transaction with currency " + transaction.currency + " cannot be added to Position with currency " + self.currency)

        #Validate Direction
        if transaction.direction == "sell":
            if self.amount < 1:
                raise ValueError("Transaction of type sell cannot be added to a closed position")
            elif self.amount < transaction.amount:
                raise ValueError("Transaction of type sell and quantity " + str(transaction.amount) + " cannot be added to position of quantity " + str(self.amount))

    def validate_args(self, transaction):
        if transaction.direction == "sell":
            raise ValueError("Transaction of type sell cannot be added to a new position")