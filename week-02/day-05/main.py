from Empolyee_analysis import Employee_analysis
from Extract_data import Extract_data


csv_file_name = "C:\\Users\\Ray_Zhang\\greenfox\\Unicorn-raya\\week-02\\day-05\\real_logs.csv"
#get employers data,and the information should be ordered
Ed = Extract_data(csv_file_name)
#could have test part here 
Ed.get_employers()
employers = Ed.package_employers()
#write specifications here
Ea = Employee_analysis(employers)
Ea.find_average_arrival_time()
print(Ea.printArrivals())

#could add some tools for visualization, like matplotlib?


# matplotlib