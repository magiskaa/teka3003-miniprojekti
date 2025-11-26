import sqlite3
from lisaa import Lisaa

class App:
    def __init__(self, io):
        self.io = io

    def connect_db(self):
        db = sqlite3.connect("data/tietokanta.sqlite")
        db.row_factory = sqlite3.Row
        cursor = db.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS 
            citations (
                cite_key TEXT UNIQUE PRIMARY KEY,
                author TEXT,
                title TEXT,
                year INTEGER
            )
        """)
        db.commit()

        return db, cursor

    def run(self):
        db, cursor = self.connect_db()

        while True:
            komento = self.io.read("\nKirjoita komento (esim. lisaa article): ")

            if not komento:
                break

            if komento.startswith("lisaa"):
                kom, arg = komento.split(" ")
                self.io.write(f"\nKomento: {kom}")
                self.io.write(f"Argumentti: {arg}")

                # Esim.
                # lisaa = Lisaa(kom, arg, db)
                # lisaa.run() -> kysyy käyttäjältä author, title, year...

        db.close()
