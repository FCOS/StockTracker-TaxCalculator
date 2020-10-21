import logging

class Transaction:
    def __init__(self, name, date, direction, amount, price, currency="Euro"):
        self.validate_args(name, date, direction, amount, price, currency)

        self.name = name
        self.date = date
        self.direction = direction.lower()
        self.amount = amount
        self.price = price
        self.currency = currency
        self.open = amount
        self.profit = 0

        

    def __str__(self):
        return_str = self.name + ": "
        return_str += self.direction + " "
        return_str += str(self.amount) 
        return_str += "@"
        return_str += str(self.price) + " "
        return_str += self.currency + ", "
        return_str += self.date + ", "
        return_str += "Open: " + str(self.open)
        if self.direction == "sell":
            return_str += ", profit: " + str(self.profit)
        
        return return_str
    
    def validate_args(self, name, date, direction, amount, price, currency):
        #Validate name
        if type(name) is not str:
            raise ValueError("Data passed into name must be of type str. Recieved " + str(type(name)))
        
        #Validate date
        if type(date) is not str:
            raise ValueError("Data passed into date must be of type str. Recieved " + str(type(date)))
        
        #Validate direction
        if type(direction) is str:
            if direction.lower() != "buy" and direction.lower() != "sell":
                raise ValueError("Data passed into direction must be buy or sell. Recieved " + direction)
        else:
            raise ValueError("Data passed into direction must be of type str. Recieved " + str(type(direction)))
        
        #Validate amount
        if type(amount) is int:
            if amount < 1:
                raise ValueError("Provided amount was less than 1. Recieved " + str(amount))
        else:
            raise ValueError("Data passed into amount must be of type int. Recieved " + str(type(amount)))

        #Validate price
        if type(price) is float or type(price) is int:
            if price <= 0:
                raise ValueError("Provided price must be greater than 0. Recieved " + str(price))
        else:
            raise ValueError("Data passed into amount must be a numberic data type. Recieved " + str(type(price)))

        #Validate currency
        if type(currency) is str:
            if currency.lower() != "euro" and currency.lower() != "gbx" and currency.lower() != "dollar":
                raise ValueError("Data passed into currency must be euro, dollar or gbx. Recieved " + currency)
        else:
            raise ValueError("Data passed into currency must be of type str. Recieved " + str(type(currency)))
