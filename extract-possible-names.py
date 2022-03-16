import sys
import psycopg2
from psycopg2 import OperationalError, Error
import dbconfig

def create_connection():
    connection = None
    try:
        connection = psycopg2.connect(
            database=dbconfig.db,
            user=dbconfig.user,
            password=dbconfig.password,
            host=dbconfig.host,
            port=dbconfig.port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection


def representation_exists(token, connection): 
    if "'" in token: 
        return True

    cursor = connection.cursor()
    try:
        cursor.execute("select count(*) from representations where representation = '%s'" % (token.lower()))
        return cursor.fetchone()[0]>0
    except Error as e:
        print(f"The error '{e}' occurred")
        raise e
 

def process_tokens(filename):
    connection = create_connection()
    token_positions = {}
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            tokens = line.split(sep = '\t')
            token_position = tokens[4]
            normal_token = tokens[5]
            token_positions[normal_token] = set(token_position)|token_positions[normal_token] if normal_token in token_positions else set(token_position)
    for i in sorted(token_positions.items(), key = lambda x: x[0]):
        positions = i[1]  
        if len(positions) == 1 and list(positions)[0] == '0':
            token = i[0]
            if not representation_exists(token, connection):
                print(token)

sys.stdout.reconfigure(encoding='utf-8')
process_tokens(sys.argv[1])
