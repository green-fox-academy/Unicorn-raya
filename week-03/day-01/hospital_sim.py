import random

class Patient:
    def __init__(self):
        self.severity = random.randint(1,10) 
    
    def getSeverity(self):
        return self.severity

    def treatPatient(self):
        if self.severity > 0:
            self.severity -= 1
        
class My_Queue:
    def __init__(self,mq = []):
        self.m_queue = mq
        self.valid_index = 0
    
    def add(self,patient):
        self.m_queue.append(patient)

    def dequeue(self):
        if self.valid_index  < len(self.m_queue):
            self.valid_index += 1
            return self.m_queue[self.valid_index - 1]
        else:
            print("Empty queue")
    
    def traversal_next(self):
        if len(self.m_queue) > 1:
            return self.m_queue[self.valid_index + 1]
        else:
            print("Not more patients")
    
class SafeQueue(My_Queue):
    def __init__(self):
        super().__init__(self)

    def find_highest_one(self):
        tmp = -1
        candidate = Patient()
        for p in self.m_queue:
            if p.getSeverity() > tmp:
                tmp = p.getSeverity()
                candidate = p
        return candidate
    
    def dequeue(self):
        self.
        

    
class ClassicQueue(My_Queue):
    def __init__(self):
        super().__init__(self)
        
p1 = Patient()
p2 = Patient()
p3 = Patient()
p4 = Patient()
