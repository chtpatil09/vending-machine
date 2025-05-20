
from vending_machine.inventory import Inventory
from vending_machine.utils import is_valid_coin, calculate_change
from vending_machine.config import PRICES

class VendingMachine:
    def __init__(self):
        self.inventory = Inventory()
        self.balance = 0

    def insert_coin(self, coin):
        if not is_valid_coin(coin):
            raise ValueError("Invalid coin.")
        self.balance += coin

    def buy(self, item):
        if not self.inventory.is_available(item):
            return "Out of stock"
        price = PRICES[item]
        if self.balance < price:
            return f"Insufficient balance. {price - self.balance} more needed."
        self.inventory.reduce(item)
        self.balance -= price
        change = calculate_change(self.balance)
        self.balance = 0
        return {"item": item, "change": change}
