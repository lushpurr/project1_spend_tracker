import unittest
from models.tag import Tag

class TestTag(unittest.TestCase):
    def setUp(self):
        self.tag1 = Tag('Fuel', 1)

    def test_tag_has_category(self):
        self.assertEqual("Fuel", self.tag1.category)

    def test_tag_has_id(self):
        self.assertEqual(1, self.tag1.id)