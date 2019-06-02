'''
operation of views in db
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

# Who sent the most messages to the thanks channel?
def view_creation_1(db_connection):
    cursor = db_connection.cursor()
    create_view_query = """ create view most_thanks (user_id, mess_nums) as (
        select user_id,count(*) from messages group by user_id order by count(*) desc limit 20
    ); 
    """
    cursor.execute(create_view_query)
    connection.commit()
    print("view created successfully in DB_postgres")

# Which emoji is the most common as reaction in the thanks channel?
def view_creation_2(db_connection):
    cursor = db_connection.cursor()
    create_view_query = """ create view most_emoji (emoji, times) as (
         select reaction,count(reaction)
         from reactions group by reaction order by count(reaction) desc limit 20
    ); 
    """
    cursor.execute(create_view_query)
    connection.commit()
    print("view created successfully in DB_postgres")

# Who reacted to the most messages?
def view_creation_3(db_connection):
    cursor = db_connection.cursor()
    create_view_query = """ create view most_message (user_id, times) as (
            select user_id,count(message_id) 
            from reactions group by user_id 
            order by count(message_id) desc limit 20
    ); 
    """
    cursor.execute(create_view_query)
    connection.commit()
    print("view created successfully in DB_postgres")

# Who is the most mentioned person in the thanks channel?
def view_creation_4(db_connection):
    cursor = db_connection.cursor()
    create_view_query = """ create view most_mentioned (user_id,times) as (
            select user_id,count(message_id) from mentions
            group by user_id order by count(message_id) desc limit 20
    ); 
    """
    cursor.execute(create_view_query)
    connection.commit()
    

def get_most_emoji(db_connection): 
    cursor = db_connection.cursor()
    view_table = """select * from most_emoji"""
    cursor.execute(view_table)
    connection.commit()
    records = cursor.fetchall()
    return records


def get_most_message(db_connection): 
    cursor = db_connection.cursor()
    view_table = """select * from most_message"""
    cursor.execute(view_table)
    connection.commit()
    records = cursor.fetchall()
    return records


def get_most_thanks(db_connection): 
    cursor = db_connection.cursor()
    view_table = """select * from most_thanks"""
    cursor.execute(view_table)
    connection.commit()
    records = cursor.fetchall()
    return records

def get_most_mentioned(db_connection): 
    cursor = db_connection.cursor()
    view_table = """select * from most_mentioned"""
    cursor.execute(view_table)
    connection.commit()
    records = cursor.fetchall()
    return records
# Which message got the most reactions in the thanks channel?
# Which day was the most active in the channel?
# Who is the most active in the channel?
# What is the average daily message in the channel?
# Which post received the most positive emoji in the random channel?
# Which message is the most positively reacted in the random channel? (subtract negative emojis)
# Which message has the highest positive/negative ratio in the random channel?
# At which time of the day are the employees the most active?

def close_db(db_connnection):
    if(db_connnection):
        cursor = db_connnection.cursor()
        cursor.close()
        db_connnection.close()
        print("db_project connection is closed")


connection = init_db()
#view_creation_1(connection)
#view_creation_2(connection)
#view_creation_3(connection)
#view_creation_4(connection)
emoji = get_most_emoji(connection)
message = get_most_message(connection)
mention = get_most_mentioned(connection)
thank = get_most_thanks(connection)

close_db(connection)

