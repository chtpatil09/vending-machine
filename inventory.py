
class Inventory:
    def __init__(self):
        self.stock = {
            'still': 3,
            'fizzy': 3
        }

    def is_available(self, item):
        return self.stock.get(item, 0) > 0

    def reduce(self, item):
        if self.is_available(item):
            self.stock[item] -= 1
            return True
        return False

    def refill(self, item, quantity):
        self.stock[item] += quantity
