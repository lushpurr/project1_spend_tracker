import unittest
from models.transaction import Transaction

class TestTransaction(unittest.TestCase):



    def setUp(self):
        self.transaction1 = Transaction(10.00, 'BP', 'Fuel', 1)

    def test_transaction_has_amount(self):
        self.assertEqual(10.00, self.transaction1.amount)

    def test_transaction_has_merchant(self):
        self.assertEqual("BP", self.transaction1.merchant)

    def test_transaction_has_tag(self):
        self.assertEqual("Fuel", self.transaction1.tag)

    def test_transaction_has_id(self):
        self.assertEqual(1, self.transaction1.id)




