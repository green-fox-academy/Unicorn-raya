from Animal_protection import Animal
import unittest

class Animal_test(unittest.TestCase):
    def setUp(self):
        self.a1 = Animal("cat")
        self.a2 = Animal("Dog",True,3)
    
    def test_Animal_name(self):
        self.assertEqual(self.a1.name,"cat")
        self.assertEqual(self.a2.name,"Dog")

    def test_Animal_heal(self):
        self.assertEqual(self.a1.isAdoptable(),False)
        self.assertEqual(self.a2.isAdoptable(),True)

    def test_Animal_cost(self):
        self.assertEqual(self.a1.healCost,1)
        self.assertEqual(self.a2.healCost,3)

if __name__ == '__main__':
    unittest.main()

 