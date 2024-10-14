
import pandas as pd
import sqlite3

from sqlite3 import Connection, Cursor

csv_file_path = r'C:\Users\sergio\Desktop\cocjornada\database\Alunos_Jornada.csv'
db_file_path = r'C:\Users\sergio\Desktop\cocjornada\final_db.sqlite3'

data_frame_columns_list = ['registration', 'student_name', 'anosemestre', 'student_class']

csv_enconding = 'ISO-8859-1'
delimiter = ';'

table_name = 'guest_student'

query_table_structure = f'''
CREATE TABLE {table_name} (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    registration INTEGER,
    student_name TEXT,
    anosemestre INTEGER,
    student_class TEXT
);
'''


def create_data_frame(csv_file_path:str, csv_enconding: str, delimiter: str, data_frame_columns_list: str):
    data_frame = pd.read_csv(csv_file_path, encoding=csv_enconding, delimiter=delimiter)
    data_frame.columns = data_frame_columns_list
    return data_frame

def create_connection(db_file_path: str): 
    db_connection = sqlite3.connect(db_file_path)
    return db_connection

def create_cursor(db_connection: Connection):
    cursor = db_connection.cursor()
    return cursor

def create_query_table(cursor: Cursor, query_table_structure: str):
    cursor.execute(f"DROP TABLE IF EXISTS {table_name};")
    create_table_query = query_table_structure
    cursor.execute(create_table_query)


def populate_db(csv_file_path: str, db_file_path: str, data_frame_columns: str, csv_enconding:str, table_name: str, query_table_structure: str, delimiter=None):
    data_frame = create_data_frame(csv_file_path, csv_enconding, delimiter, data_frame_columns)

    db_connection = create_connection(db_file_path)
    cursor = create_cursor(db_connection)

    query_table = create_query_table(cursor, query_table_structure)

    data_frame.to_sql(table_name, db_connection, if_exists='append', index=False)

    db_connection.commit()
    db_connection.close()

populate_db(csv_file_path, db_file_path, data_frame_columns_list, csv_enconding, table_name, query_table_structure, delimiter)
