import unittest
from cow_bull_game import CBGame

class Test_CBGame(unittest.TestCase):
    def setUp(self):
        self.example = CBGame()
        self.answer = self.example.getAnswer()
        self.status = self.example.getStatus()
    
    def diff_num4each_position(self,digits):
        numberIneachPos = []
        for di in digits:
            numberIneachPos.append(di)
        for i in range(len(numberIneachPos)):
            for j in range(i + 1,len(numberIneachPos)):
                if numberIneachPos[i] == numberIneachPos[j]:
                    return False
        return True
    
    def test_each_digit_diff(self):
        self.assertTrue(self.diff_num4each_position(self.answer))
    
    def test_status(self):
        self.assertEquals(self.status, "playing")
        self.assertEquals(self.status, "finished")
    
    
        

if __name__ == '__main__':
    unittest.main()

#path = \.Unicorn-raya\.week-03\.day-02\.Cow_Bulls