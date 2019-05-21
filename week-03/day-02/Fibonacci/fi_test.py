import unittest
from fi import Fibonacci

class Fibonacci_test(unittest.TestCase):
    def test_fibo(self):
        self.assertEqual(Fibonacci().fibo(5),5)
        self.assertEqual(Fibonacci().fibo(0),0)
        self.assertEqual(Fibonacci().fibo(1),1)

if __name__  == '__main__':
    unittest.main()