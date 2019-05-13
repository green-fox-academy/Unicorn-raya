# Counter
# Create Counter class
# which has an integer field value
# when creating it should have a default value 0 or we can specify it when creating
# we can add(number) to this counter another whole number
# or we can add() without parameters just increasing the counter's value by one
# and we can get() the current value
# also we can reset() the value to the initial value
# Check if everything is working fine with the proper test
# Download test_counter.py and place it next to your solution
# Run the test file as a usual python program

class Counter(object):
    def __init__(self,number = 0):
        self.default_number = number
        self.count_number = self.default_number

    def add(self,number = 1):
        return self.count_number + number
    
    def get(self):
        #print(f"current number is: {self.count_number}")
        return self.count_number

    def reset(self):
        self.count_number = self.default_number
        return self.count_number

test_counter = Counter(7)
test_counter.get()

test_counter.add(20)
test_counter.get()

test_counter.reset()
test_counter.get()
