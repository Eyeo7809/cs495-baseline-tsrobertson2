import unittest
from utils import firstUniqueChar

class TestUtils(unittest.TestCase):
    
    def test_unique_char(self):
        self.assertEqual(firstUniqueChar("cow"), ['c', 'o', 'w'])
    
    def test_multiple_letters(self):
        self.assertEqual(firstUniqueChar("chocolate"), ['c', 'h', 'o', 'l', 'a', 't', 'e'])
    
    def test_cases(self):
        self.assertEqual(firstUniqueChar("HeLlO WorLD"), ['h', 'e', 'l', 'o', 'w', 'r', 'd'])


if __name__ == '__main__':
    unittest.main()