import unittest
from models.tag import Tag

class TestTag(unittest.TestCase):
    def setUp(self):
        self.tag1 = Tag('Fuel')

    def test_tag_has_category(self):
        self.assertEqual("Fuel", self.tag1.category)