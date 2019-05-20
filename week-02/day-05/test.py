# # # #-*-coding:utf-8-*- 

# 迭代到 employer ： emp_id ? 继续迭代 time_db [] -> {
#                                             time_info_1 -> ... day hour minute second
#                                             time_info_2 -> ... day hour minute second
#                                             time_info_3 -> ... day hour minute second
#                                             time_info_4 -> ... day hour minute second
#                                             .               判断 ：当前day 是否为day_index,即 相同day的所有信息的第一条信息，并记录下来
#                                                                    若不是， 则 day_index += 1   跳到下一天
#                                                             当跳出最后一天的时候，循环结束，跳到下一个employer
#                                             .
#                                             .


#                                             }

lst = [1,23, "asdaasdas",{"yahaha":12}]

print(lst[3])




