'''
relation table for users and messages,double FK, no PK
'''
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

def db_mentions_creation(db_connection):
    cursor = db_connection.cursor()
    create_table_query = ''' create table mentions(      
        USER_ID    VARCHAR(255)                NULL,
        MESSAGE_ID    TEXT                 NULL     
    );'''
    cursor.execute(create_table_query)
    connection.commit()
    print("Table messages created successfully in DB_postgres")

def db_mentions_insertion(db_connnection,json_file_name_1):
    json_file = open(json_file_name_1,'r')
    messages = json.load(json_file)
    cursor = db_connnection.cursor()
    insertion = """INSERT INTO mentions (USER_ID,MESSAGE_ID) VALUES (%s,%s)"""       
    for message in messages:
        text = message["text"]
        r = re.compile(r"<@(\w{9})>")
        users =r.findall(text)
        for user in users:
            if "client_msg_id" in message.keys():
                cursor.execute(insertion,(user,message["client_msg_id"]))

    db_connnection.commit()
    json_file.close()

def close_db(db_connnection):
    if(db_connnection):
        cursor = db_connnection.cursor()
        cursor.close()
        db_connnection.close()
        print("db_project connection is closed")

json_file_1 = 'C:\\Users\\Ray_Zhang\\greenfox\\Unicorn-raya\\week-04\\day-04\\thanks.json'
#json_file_3 = "week-04\day-04\gfa-team-thanks-replies.json"

connection = init_db()

db_mentions_creation(connection)
db_mentions_insertion(connection,json_file_1)

#print_db(connection)

close_db(connection)
