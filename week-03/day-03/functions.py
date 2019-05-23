import csv

def splitdata2list():
    filename = open("Unicorn-raya\week-03\day-03\products.csv")
    tmp_list = []
    for line in filename:
        tmp_list.append(line)
    filename.close()
    product_names,prices,qtys = [],[],[]

    for index in range(1,len(tmp_list)):
        tmp_string = list(tmp_list[index].split(";"))
        product_names.append(tmp_string[1])
        prices.append(tmp_string[2])
        qtys.append(tmp_string[3].strip("\n")) 
    return product_names,prices,qtys

def search_by_product_name(p_name,p_names,prices,qtys):
    price_list = []
    qtys_list = []  
    for index in range(len(p_names)):
        if p_names[index] == p_name:
            price_list.append(prices[index])
            qtys_list.append(qtys[index])
    result_string = []
    for index in range(len(price_list)):
        tmp = "prices :" + price_list[index] + " qtys: "+qtys_list[index]
        result_string.append(tmp)
    return result_string

def search_by_price(price,p_names,prices,qtys):
    product_list =[]
    qtys_list = []
    for index in range(len(prices)):
        if prices[index] == price:
            product_list.append(p_names[index])
            qtys_list.append(qtys[index])
    result_string = []
    for index in range(len(product_list)):
        tmp = "procuctName :" + product_list[index] + " qtys: "+qtys_list[index]
        result_string.append(tmp)

    return result_string

def search_by_qtys(qty,p_names,prices,qtys):
    product_list = []
    qtys_list = []
    for index in range(len(qtys)):
        if qtys[index] == qty:
            product_list.append(p_names[index])
            qtys_list.append(prices[index])
    result_string = []
    for index in range(len(product_list)):
        tmp = "procuctName :" + product_list[index] + " prices: "+qtys_list[index]
        result_string.append(tmp)

    return result_string

product_names,prices,qtys = splitdata2list()
#print(product_names)
# print(prices)
# print(qtys)

p_name = "display"
price = "70"
qty = "10"

print(search_by_price(price,product_names,prices,qtys))
print(search_by_product_name(p_name,product_names,prices,qtys))
print(search_by_qtys(qty,product_names,prices,qtys))
   