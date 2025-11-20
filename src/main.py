import sqlite3

if __name__ == "__main__":
    # Luo tietokannan, Tee tämä app luokassa
    conn = sqlite3.connect("data/tietokanta.sqlite")
    cursor = conn.cursor()

    # Esimerkkipöytä, myös app luokassa ja oikeilla jutuilla.
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
    conn.commit()
    
    print("Hello world")