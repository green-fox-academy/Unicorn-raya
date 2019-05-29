import psycopg2
from psycopg2 import Error
import sys
command = ""
info =""
full_command =""
if len(sys.argv) > 1:
    command = sys.argv[1]
    info = " ".join(sys.argv[2:])
    full_command = " ".join(sys.argv[1:])

def init_db():
    connection = psycopg2.connect(host = "127.0.0.1",# or could be localhost
                                database = "postgres",
                                user = "postgres",
                                password = "5571909")
     
    cursor = connection.cursor()
    drop_table = """ drop table Music""" # could be checked by if statement
    cursor.execute(drop_table)
    connection.commit()

    create_table_query = ''' create table Music(
        ID BIGSERIAL PRIMARY KEY     NOT NULL,
        ARTIST      TEXT       NOT NULL,
        TITLE     TEXT     NOT NULL,
        PLAYING   INT   DEFAULT  0
    );'''

    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully in DB_postgres")
    db_insert_query = """ INSERT INTO Music (ARTIST,TITLE) VALUES (%s,%s) """
    sample_data = ["Ed aaa","songs1111"]
    cursor.execute(db_insert_query,sample_data)
    connection.commit()    
    return connection 

# message format is like: Ed Sheeran: I Don't care 
def add_song(message,db_connection):
    info =list(message.split(":"))
    cursor = db_connection.cursor()
    db_insert_query = """ INSERT INTO Music (ARTIST,TITLE) VALUES (%s,%s) """
    # table name could be a parameter *_*
    cursor.execute(db_insert_query,info)
    db_connection.commit()
    print("Record inserted successfully")

# keyword could be: 
# --artist "Ed" // it should list all the songs which belongs to an artist who's name contains "Ed"
# "Ed"          // it should list all the songs who's has the title or artist contains "Ed"
def list_songs(keyword,db_connection):
    cursor = db_connection.cursor()
    db_execute_query = ""
    if keyword == "":
        db_execute_query = """ SELECT * FROM Music """
        cursor.execute(db_execute_query)
        record = cursor.fetchall()
        print(record)
    elif list(keyword.split(" "))[0] == "--artist":# reco like "--artist "Ed"'
        db_execute_query = """ SELECT TITLE,ARTIST FROM Music WHERE ARTIST LIKE %s"""
        artist = list(keyword.split(" "))[1][1:-1] + '%'
        cursor.execute(db_execute_query,(artist,))
        record = cursor.fetchall()
        print(record)
    else:
        db_execute_query = """ SELECT TITLE,ARTIST FROM Music where TITLE LIKE %s or ARTIST LIKE %s"""
        keyword += '%'
        cursor.execute(db_execute_query,(keyword,keyword,))
        record = cursor.fetchall()
        print(record)

def remove_id_from_db(m_id, db_connection):
    cursor = db_connection.cursor()
    db_execute_query = """ DELETE FROM Music where ID = %s"""
    cursor.execute(db_execute_query,str(m_id))
    print(f'id: {m_id} delete successfully')

def play_song_by_id(m_id,db_connection):
    cursor = db_connection.cursor()
    check_any_playing_song = """SELECT ID FROM Music where PLAYING = 1 """ 
    cursor.execute(check_any_playing_song)
    record = cursor.fetchall()
    
    if len(record) != 0:
        stop_current_playing = """UPDATE Music SET PLAYING = 0 WHERE ID = %s """
        cursor.execute(stop_current_playing,record[0])
        print(f"song id: {record[0][0]} has been stopped")
    db_play_query = """ SELECT TITLE,PLAYING FROM Music where ID = %s """
    cursor.execute(db_play_query,str(m_id))
    print(f"current playing the {cursor.fetchone()[0]} ")
    set_playing_to_1 = """UPDATE Music SET PLAYING = 1 WHERE ID = %s """
    cursor.execute(set_playing_to_1,(m_id,))

#db_connection is the connection that u link with database
def close_db(db_connnection):
    if(db_connnection):
        cursor = db_connnection.cursor()
        cursor.close()
        db_connnection.close()
        print("PostgreSQL connection is closed")

connection = init_db()
if command == "a":
    add_song(info,connection)
elif command == "d":
    int_info = int(info)
    remove_id_from_db(int_info,connection)
elif command == "--artist":
    print(full_command)
    list_songs(full_command,connection)
elif command == "p":
    play_song_by_id(int(info),connection)
else:
    list_songs(full_command,connection)
close_db(connection)
# connection = init_db()
# add_song("Ed Sheeran:I Don't care",connection)
# add_song("name111:song111",connection)
# add_song("name444:EdsongEdss",connection)
# add_song("name222:song222",connection)
# add_song("name333:song333",connection)
# # remove_id_from_db(2,connection)
# list_songs('',connection)
# list_songs('--artist "Ed"',connection)
# list_songs("Ed",connection)
# play_song_by_id(2,connection)
# play_song_by_id(3,connection)
# close_db(connection)