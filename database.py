import sqlite3

def connect_to_database(database_name):
    conn = sqlite3.connect(database_name)
    return conn

def create_tables(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            lifestyle TEXT,
            eating_habits TEXT,
            exercise_routine TEXT,
            mental_wellbeing TEXT,
            medical_conditions TEXT
        )
    ''')
    conn.commit()

def insert_user_inputs(conn, user_inputs):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO users (username, lifestyle, eating_habits, exercise_routine, mental_wellbeing, medical_conditions)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        user_inputs['username'],
        user_inputs['lifestyle'],
        user_inputs['eating_habits'],
        user_inputs['exercise_routine'],
        user_inputs['mental_wellbeing'],
        user_inputs['medical_conditions']
    ))
    conn.commit()

def retrieve_user_inputs(conn, username):
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM users WHERE username = ?
    ''', (username,))
    user_data = cursor.fetchone()
    return user_data
