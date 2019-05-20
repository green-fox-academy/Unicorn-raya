from employee import Employee
from Time import Time_information
import csv

class Extract_data:
    def __init__(self,csv_file_name,employees = []):
        self.csv_file_name = csv_file_name
        self.employees = employees
    
    #check whether id is in the employees' list, return its index if true, otherwise false
    def check_exist_id(self,ep_id):
        for data_index in range(len(self.employees)):
            if ep_id == self.employees[data_index].ep_ID:
                return data_index
        return -1

    def get_employers(self):
        file = open(self.csv_file_name)
        csv_file = csv.reader(file)
        for data in csv_file:
            tmp_ep_id = data[12]
            tmp_ep_date_time = data[1]
            tmp_ep_time_info = data[5][:8]
            time_buffer = list(tmp_ep_date_time[:10].split("."))
            time_buffer_2 = list(tmp_ep_date_time[12:].split(":"))
            tmp_time_class = Time_information(int(time_buffer[0]),int(time_buffer[1]),int(time_buffer[2]),int(time_buffer_2[0]),int(time_buffer_2[1]),int(time_buffer_2[2]),tmp_ep_time_info)
            tmp_time_list = []
            tmp_time_list.append(tmp_time_class)
            index = self.check_exist_id(tmp_ep_id)
            if index != -1:
                self.employees[index].add_new_time_in_emp(tmp_time_class)
            else:
                self.employees.append(Employee(tmp_ep_id,tmp_time_list))
        file.close()

    def print_emp(self):
        for i in self.employees:
            i.print_emp_info()

    def get_employer_massage(self,emp_id):
        self.employees[self.check_exist_id(emp_id)].print_emp_info()
    
    def package_employers(self):
        return self.employees 
    
csv_file_name = "C:\\Users\\Ray_Zhang\\greenfox\\Unicorn-raya\\week-02\\day-05\\real_logs.csv"

ee = Extract_data(csv_file_name)
ee.get_employers()
#print(len(ee.employees))
#id = "00115:46240"
#ee.get_employer_massage(id)
#ee.print_emp()       
    