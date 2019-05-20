# Question Suggestions:
    # What is the average arrival time?
    # What is the median of the arrivals?
    # What is the deviation of the arrivals?
    # What is the average late in minutes?
    # What is the median of the late arrivals?
    # Who was late the most in overall in minutes?
    # Who was late the most times?
    # What is the average late in minutes?
    # Who leaves the office most times a day (avg)?
    # Which day has the most late arrivals?
    # Are there any days when nobody was late?
    # What is the average time to get to the 2nd floor?
    # What is the average time to get to the 3rd floor?
    # Who should we terminate the contract with?

from employee import Employee
from Extract_data import Extract_data
class Employee_analysis:
    def __init__(self,employees = []):
        self.employees = employees
        self.emp_arrivals_info = []
        self.late_time = 0
        self.late_employee_id = ""

    def printArrivals(self):
        for i in self.emp_arrivals_info:
            print(f"ID: {i[0]}, at day :{i[1]}")
            print(i[2].print_time())
               
    def getEmpArrInfo(self):
        return self.emp_arrivals_info

    # find average arrival time in the data
    def find_average_arrival_time(self): 
        for emp in self.employees:
            group = []
            group.append(emp.get_epID())
            start_day = emp.get_timedb()[0].getDay()
            group.append(start_day)
            group.append(emp.get_ep_info_by_day(start_day)[0])
            self.emp_arrivals_info.append(group)

    # find find average arrival time at sp date
    def find_average_arrival_time_in_spday(self,date_time):
        pass

    def find_most_late_guy(self):
        pass
    #count the most times of door
    def count_main_door_times(self):
        pass
    #find the late at specify day, type if date_time in file Time.py        
    def find_late_guys_in_specify_day(self,date_time):
        pass





    
