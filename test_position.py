from transaction import Transaction
from position import Position
import logging

logging.basicConfig(level=logging.INFO)

shell_holdings = Position(Transaction("RDSA", "08/05/2020", "buy", 220, 12.233))
print(shell_holdings)


shell_holdings.add_transaction(Transaction("RDSA", "08/05/2020", "sell", 190, 13.233))
print(shell_holdings)
shell_holdings.add_transaction(Transaction("RDSA", "08/05/2020", "buy", 1, 10))
print(shell_holdings)
shell_holdings.add_transaction(Transaction("RDSA", "08/05/2020", "buy", 2, 20))
print(shell_holdings)
 
shell_holdings.print()

shell_holdings.update_position()