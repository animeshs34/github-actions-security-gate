import sqlite3
import os

def get_user_data(user_id):
    # SQL Injection vulnerability
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    print(f"Executing query: {query}")
    cursor.execute(query)
    return cursor.fetchone()

def run_system_command(cmd):
    # Command Injection vulnerability
    os.system(cmd)

if __name__ == "__main__":
    uid = input("Enter user ID: ")
    print(get_user_data(uid))
