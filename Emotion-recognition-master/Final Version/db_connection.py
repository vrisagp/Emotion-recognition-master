import sqlite3

def get_connection():
    conn = sqlite3.connect('tourism_agency.db')
    return conn
