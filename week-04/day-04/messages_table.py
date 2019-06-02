'''
This file is used for operating table messages, must be done at second step to ensure 
the FK in other table and the link with users table
'''
import psycopg2
from psycopg2 import Error
import json

def init_db():
    connection = psycopg2.connect(host = "127.0.0.1",# or could be localhost
                                database = "project",
                                user = "postgres",
                                password = "5571909")
     
    return connection

#create MESSAGES table
def db_messages_creation(db_connection):
    cursor = db_connection.cursor()
    create_table_query = ''' create table messages(
        ID         VARCHAR(255)         NOT NULL,       
        USER_ID    VARCHAR(255)         NOT NULL,
        MESSAGE    TEXT                 NULL,
        CHANNEL    TEXT                 NULL,
        SEND_AT    TEXT                 NULL, 
        CONSTRAINT MAESSAGES_PK PRIMARY KEY(ID)
    );'''
    cursor.execute(create_table_query)
    connection.commit()
    print("Table messages created successfully in DB_postgres")
    
def db_messages_insertion(db_connnection,json_file_name_1):
    #insert data from random.json file
    json_file = open(json_file_name_1,'r')
    messages = json.load(json_file)
    cursor = db_connnection.cursor()
    insertion = """INSERT INTO messages (ID,USER_ID,MESSAGE,CHANNEL,SEND_AT) VALUES (%s,%s,%s,%s,%s)"""       
    for message in messages:
        if "client_msg_id" in message.keys():
            cursor.execute(insertion,(message["client_msg_id"],message["user"],message["text"],"random",message["ts"]))
    db_connnection.commit()
    json_file.close()

#drop all tables 
def db_messages_drop(db_connection):
    cursor = db_connection.cursor()
    drop_table = """ drop table messages""" 
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
# db_messages_drop(connection)
db_messages_creation(connection)
db_messages_insertion(connection,json_file_1)

close_db(connection)
