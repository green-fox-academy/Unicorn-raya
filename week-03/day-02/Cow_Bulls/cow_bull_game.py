import random
class CBGame:
    def __init__(self):
        self.number_list = [0,1,2,3,4,5,6,7,8,9]
        self.num_lst_length = 9
        self.digits_length = 4
        self.digits = 0
        self.status = "playing"
        for index in range(self.digits_length):
            tmp = random.randint(0,self.num_lst_length - index)
            self.digits = 10 * self.digits + self.number_list[tmp]
            self.number_list.pop(tmp)
        self.digits = str(self.digits)
    
    def reset(self):
        self.number_list = [0,1,2,3,4,5,6,7,8,9]

    def getStatus(self):
        return self.status

    def getAnswer(self):
        return self.digits

    def play(self,guess_number):
        tmp_guess_number = str(guess_number)
        bulls = 0
        cows = 0
        for digit_index in range(len(tmp_guess_number)):
            if tmp_guess_number[digit_index] == self.digits[digit_index]:
                cows += 1
                continue
            if tmp_guess_number[digit_index] in self.digits:
                bulls += 1
                continue
            if cows == 4:
                self.status = "finished"
                self.reset()
        return f"{cows} cows, {bulls} bulls"

# cb = CBGame()
# print(type(cb.getAnswer()))
# print(len(cb.getAnswer()))
# print(cb.play(1204))       
