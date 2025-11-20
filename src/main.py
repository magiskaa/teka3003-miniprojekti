import sqlite3

# Connect to a database file (will create if it doesn't exist)
conn = sqlite3.connect("data/tietokanta.sqlite")
cursor = conn.cursor()

# Example: create table
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
conn.commit()

print("hello world")