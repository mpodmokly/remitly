import unittest
from find_asterisk import find_asterisk

class Test(unittest.TestCase):
    def test_find_asterisk(self):
        self.assertTrue(find_asterisk("tests/test1.json"))
        self.assertFalse(find_asterisk("tests/test2.json"))
        self.assertFalse(find_asterisk("tests/test3.json"))
        self.assertFalse(find_asterisk("tests/test4.json"))
