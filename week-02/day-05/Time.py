class Time_information:
    def __init__(self,year=0.0,month=0.0,day=0.0,hour=0.0,minute=0.0,second=0.0,location = ""):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
        self.location = location
    
    def getDay(self):
        return self.day

    def getHour(self):
        return self.hour
        
    def getMinute(self):
        return self.minute   
    
    def getSecond(self):    
        return self.second

    def getLocation(self):
        return self.location
    
    def getTime_by_day(self,day):
        if day == self.day:
            return self.hour,self.minute,self.second

    def print_time(self):
        print(f"at day: {self.getDay()},{self.getHour()}:{self.getMinute()}:{self.getSecond()},pass {self.getLocation()}")
    
