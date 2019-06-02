"""
This file is used for operating table users, must be done at first step to ensure 
the FK in other table

"""
import psycopg2
from psycopg2 import Error
import json
import re

def init_db():
    connection = psycopg2.connect(host = "127.0.0.1",# or could be localhost
                                database = "project",
                                user = "postgres",
                                password = "5571909")
     
    return connection

#create USERS table
def db_users_creation(db_connection):
    cursor = db_connection.cursor()
    create_table_query = ''' create table users(
        USER_ID    VARCHAR(255)        NOT NULL,
        CONSTRAINT Users_PK PRIMARY KEY(USER_ID)
    );'''
    cursor.execute(create_table_query)
    connection.commit()
    print("Table users created successfully in DB_postgres")

#insert values from gfa-team-random.json and gfa-team-thanks.json into USERS table
#delicate data should be merged by ignore statement
def db_users_insertion(db_connnection,json_file_name_1):
    json_file = open(json_file_name_1,'r')
    messages = json.load(json_file)
    users = []
    for mss in messages:
        if "user" in mss.keys():
            users.append(mss["user"])
        if "text" in mss.keys():
            text = mss["text"]
            r = re.compile(r"<@(\w{9})>")
            users_in_text =r.findall(text)
            for uit in users_in_text:
                users.append(uit)
        if "reply_users" in mss.keys():
            for user in mss["reply_users"]:
                users.append(user)
        if "reactions" in mss.keys():
            if "users" in mss["reactions"]:
                for user in mss["reaction"]["users"]:
                    user.append(user)
    
    json_file.close()
    users = list(set(users))
    cursor = db_connnection.cursor()
    insertion = """INSERT INTO users (USER_ID) VALUES (%s)"""       
    for user in users:
        cursor.execute(insertion,(user,))
    db_connnection.commit()

def print_db(db_connnection):
    show_info = """select * from users"""
    cursor = db_connnection.cursor()
    cursor.execute(show_info)
    records = cursor.fetchall()
    print(records)

#drop all tables 
def db_users_drop(db_connection):
    cursor = db_connection.cursor()
    drop_table = """ drop table users""" 
    cursor.execute(drop_table)
    print("table messages is dropped successfully")
    db_connection.commit()

def close_db(db_connnection):
    if(db_connnection):
        cursor = db_connnection.cursor()
        cursor.close()
        db_connnection.close()
        print("db_project connection is closed")

json_file_1 = 'C:\\Users\\Ray_Zhang\\greenfox\\Unicorn-raya\\week-04\\day-04\\thanks.json'
#json_file_3 = "week-04\day-04\gfa-team-thanks-replies.json"

connection = init_db()
#db_users_drop(connection)
db_users_creation(connection)
db_users_insertion(connection,json_file_1)

close_db(connection)
