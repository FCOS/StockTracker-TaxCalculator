# StockTracker-TaxCalculator
Work in progress.
Programmme to track stock purchases and sells, calculate current positions, tax liablilities etc.

Consists of 3 initial classes. 

Transaction:
This is an object to represent a buy or sell order of a finanical product.
It has the following variables:
name - The name of the product (eg. APPL) 
date - date of transaction 
direction -  buy/sell 
amount - quantity of shares 
price - price of product (individual)
currency - currency of the product (default euro)

Position:
This is an object to store all transactions on a common product, as well as some summary details.
It has the following variables:
name - name of the produict inside the position
value - running cost of the position (not live value yet)
amount - amount of owned products (bought - sold)
break_even_price - average purchase value of remaining shares
currency - currency of the products
profit - cumulative profit made from this position
transactions - deque of transactions that make up the position
