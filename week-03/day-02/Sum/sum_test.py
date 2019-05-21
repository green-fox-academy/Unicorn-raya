import unittest
from sum import Sum
class Test_sum(unittest.TestCase):
    def setUp(self):
        self.sum = Sum([1,2,3,4,5]).getSum()
        self.emp_sum = Sum().getSum()
        self.one_element_list = Sum([2]).getSum()
        self.multiple_list = Sum([2,3,4,5]).getSum()
        self.none_list = Sum([None]).getSum()

    def test_sum(self):
        self.assertEqual(self.sum,15)

    def test_diff_list(self):
        self.assertEqual(self.emp_sum,0)
        self.assertEqual(self.one_element_list,2)
        self.assertEqual(self.multiple_list,19)
        self.assertEqual(self.none_list,0)

if __name__  == '__main__':
    unittest.main()