import sqlite3
import os

def get_user_data(user_id):
    # VULNERABLE: SQL Injection for demo purposes. 
    # Directly embedding user input into the query string is dangerous.
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    print(f"Executing query: {query}")
    cursor.execute(query)
    return cursor.fetchone()

def run_system_command(cmd):
    # VULNERABLE: Command Injection for demo purposes.
    # os.system allows arbitrary command execution if input is not sanitized.
    os.system(cmd)

if __name__ == "__main__":
    uid = input("Enter user ID: ")
    print(get_user_data(uid))
