import unittest
from models.merchant import Merchant

class TestMerchant(unittest.TestCase):

    def setUp(self):
        self.merchant1 = Merchant('BP', 1)

    def test_merchant_has_name(self):
        self.assertEqual("BP", self.merchant1.name)

    def test_merchant_has_id(self):
        self.assertEqual(1, self.merchant1.id)
