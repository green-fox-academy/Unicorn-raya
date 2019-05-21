import unittest
from ana import Anagram
class Ana_test(unittest.TestCase):
    def test_ana(self):
        self.assertTrue(Anagram().ana("123","321"))

if __name__  == '__main__':
    unittest.main()