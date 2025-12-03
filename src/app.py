import sqlite3
from commands.lisaa import Lisaa
from commands.hae import Hae
from commands.generoi import Generoi

class App:
    def __init__(self, io, db_name="data/tietokanta.sqlite"):
        self.io = io
        self.db_name = db_name

    def connect_db(self):
        db = sqlite3.connect(self.db_name)
        db.row_factory = sqlite3.Row
        cursor = db.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS 
            article (
                cite_key TEXT UNIQUE PRIMARY KEY,
                author TEXT,
                title TEXT,
                journal TEXT,
                tag TEXT,
                year INTEGER,
                doi TEXT UNIQUE
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS 
            inproceedings (
                cite_key TEXT UNIQUE PRIMARY KEY,
                author TEXT,
                title TEXT,
                booktitle TEXT,
                tag TEXT,
                year INTEGER,
                doi TEXT UNIQUE
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS 
            book (
                cite_key TEXT UNIQUE PRIMARY KEY,
                author TEXT,
                title TEXT,
                year INTEGER,
                publisher TEXT,
                tag TEXT,
                doi TEXT UNIQUE
            )
        """)
        db.commit()

        return db

    def run(self):
        db = self.connect_db()

        while True:
            self.io.write("\n\nKirjoita komento ja sen perään referenssityyppi.\n"
                          "\nKäytettävissä olevat komennot: lisaa, hae, generoi"
                          "\nKäytettävissä olevat referenssityypit: article, inproceedings, book\n"
                          "\nSulje ohjelma : quit/exit")
            komento = self.io.read("> ")

            # Sulkukomento
            if komento in ("exit", "quit"):
                self.io.write("Ohjelma suljetaan...\n")
                break

            if komento.startswith("lisaa"):
                parts = komento.split(" ")
                arg = parts[1] if len(parts) > 1 else ""

                lisaa = Lisaa(arg, db, self.io)
                lisaa.run()

            elif komento.startswith("hae"):
                parts = komento.split(" ")
                hakuattr = parts[1] if len(parts) > 2 else None
                hakusana = parts[2] if len(parts) > 2 else ""

                haku = Hae(db, self.io, hakuattr, hakusana)
                haku.run()
                haku.tulosta()

            elif komento.startswith("generoi"):
                generoi = Generoi(db, self.io)
                generoi.run()

        db.close()
