
from vending_machine.config import VALID_COINS

def is_valid_coin(coin):
    return coin in VALID_COINS

def calculate_change(amount):
    coins = sorted(VALID_COINS, reverse=True)
    change = []
    for coin in coins:
        while amount >= coin:
            amount -= coin
            change.append(coin)
    return change
