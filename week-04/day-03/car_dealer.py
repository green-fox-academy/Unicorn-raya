import psycopg2
import json

def init_db():
    connection = psycopg2.connect(host = "127.0.0.1",# or could be localhost
                                database = "postgres",
                                user = "postgres",
                                password = "5571909")
     
    cursor = connection.cursor()
    # drop_table = """ drop table CarDealer""" # could be checked by if statement
    # cursor.execute(drop_table)
    connection.commit()

    create_table_query = ''' create table CarDealer(
        ID INT PRIMARY KEY     NOT NULL,
        BRAND      TEXT       NOT NULL,
        MODEL     TEXT     NOT NULL,
        YEAR   INT   DEFAULT  0,
        CONDITION TEXT  NOT NULL,
        PRICE   INT NOT NULL,
        COUNT INT NOT NULL
    );'''

    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully in DB_postgres")
    connection.commit()    
    return connection

def insert_data_by_file(json_file_name,connection):
    json_file = open(json_file_name,'r')
    cars = json.load(json_file)
    cursor = connection.cursor()
    db_insert = """INSERT INTO CarDealer VALUES (%s,%s,%s,%s,%s,%s,%s)"""
    for car in cars:
        cursor.execute(db_insert,(car['id'],car['brand'],car['model'],car['year'],car['condition'],car['price'],car['count'],))
    connection.commit() 
    json_file.close()

def remove_car(db_connnection):
    cursor = db_connnection.cursor()
    remove_query = """delete from CarDealer where count = 0"""
    cursor.execute(remove_query)
    db_connnection.commit()

def decrease_price(db_connnection):
    cursor = db_connnection.cursor()
    price_down = """update CarDealer set price = (0.8 * price) where condition = 'wreck'"""
    cursor.execute(price_down)
    db_connnection.commit()

def get_car_avg_age(db_connnection):
    cursor = db_connnection.cursor()
    avg_age = """select avg(year) from CarDealer where count <> 0"""
    cursor.execute(avg_age)
    db_connnection.commit()
    print(cursor.fetchall())    

def print_db(db_connnection):
    show_info = """select * from CarDealer"""
    cursor = db_connnection.cursor()
    cursor.execute(show_info)
    records = cursor.fetchall()
    print(records)


def close_db(db_connnection):
    drop_table = """ drop table CarDealer""" # could be checked by if statement
    db_connnection.cursor().execute(drop_table)
    connection.commit()
    if(db_connnection):
        cursor = db_connnection.cursor()
        cursor.close()
        db_connnection.close()
        print("PostgreSQL connection is closed")


connection = init_db()
filename = "week-04\day-03\cars.json"
insert_data_by_file(filename,connection)
#print_db(connection)
remove_car(connection)
decrease_price(connection)
get_car_avg_age(connection)

close_db(connection)