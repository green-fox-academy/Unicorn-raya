doors = ("A66 - 04","A66 - 12","A66 - 18")
from Time import Time_information 
class Employee:
    # time is the time class
    def __init__(self,ep_ID="",time_db = []):
        self.ep_ID = ep_ID
        
        #time_db is the set of time_infomation of current employer, and it is ordered by time acs.
        self.time_db =  time_db
        

    def get_epID(self):
        return self.ep_ID

    def get_timedb(self):
        return self.time_db

    def add_new_time_in_emp(self,time_info):
        self.time_db.append(time_info)

    def get_ep_info_by_day(self,day):
        emp_info = []
        for i in self.get_timedb():
            if i.getDay() == day:
                emp_info.append(i)
        return emp_info
        
    def print_emp_info(self):
        print(f"Employer ID: {self.ep_ID}")
        for time in self.time_db:
            time.print_time()

        
