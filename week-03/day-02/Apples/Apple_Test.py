import unittest
from apple import Apple

class TestAppleGet(unittest.TestCase):
    def test_getApple(self):
        self.assertEqual(Apple().get_apple(),"Apple")
        self.assertEqual(Apple().get_apple(),"Opple")


if __name__  == '__main__':
    unittest.main()