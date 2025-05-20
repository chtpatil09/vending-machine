
import unittest
from vending_machine.machine import VendingMachine

class TestVendingMachine(unittest.TestCase):
    def setUp(self):
        self.vm = VendingMachine()

    def test_insert_valid_coin(self):
        self.vm.insert_coin(5)
        self.assertEqual(self.vm.balance, 5)

    def test_insert_invalid_coin(self):
        with self.assertRaises(ValueError):
            self.vm.insert_coin(3)

    def test_buy_with_insufficient_funds(self):
        self.vm.insert_coin(10)
        result = self.vm.buy("fizzy")
        self.assertIn("Insufficient balance", result)

    def test_successful_purchase(self):
        self.vm.insert_coin(10)
        self.vm.insert_coin(10)
        self.vm.insert_coin(10)
        result = self.vm.buy("still")
        self.assertEqual(result["item"], "still")
        self.assertIsInstance(result["change"], list)
