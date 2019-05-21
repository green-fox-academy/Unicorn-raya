import unittest
from count_letter import Count_letter 
class CountLetter_test(unittest.TestCase):
    def test_countLetter(self):
        sample_dic ={"d":1,"i":3,"c":2}
        cl = Count_letter().count_letter("dcicii")
        # better use order_map
        self.assertEqual(cl,sample_dic)

if __name__  == '__main__':
    unittest.main()