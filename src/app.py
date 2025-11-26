import sqlite3

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
                parts = komento.split(" ")
                kom = parts[0]
                arg = parts[1] if len(parts) > 1 else ""

                self.io.write(f"\nKomento: {kom}")
                self.io.write(f"Argumentti: {arg}")

                from commands.lisaa import Lisaa
                lisaa = Lisaa(kom, arg, db, self.io)
                lisaa.run()

        db.close()
