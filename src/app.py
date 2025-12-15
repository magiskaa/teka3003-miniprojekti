import sqlite3
from commands.lisaa import Lisaa
from commands.hae import Hae
from commands.generoi import Generoi

class App:
    def __init__(self, io, db_name="data/tietokanta.sqlite", output_dir="output"):
        self.io = io
        self.db_name = db_name
        self.output_dir = output_dir
        self.is_test_mode = hasattr(self.io, 'inputs')

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
                year INTEGER,
                doi TEXT UNIQUE,
                tag TEXT
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS 
            inproceedings (
                cite_key TEXT UNIQUE PRIMARY KEY,
                author TEXT,
                title TEXT,
                booktitle TEXT,
                year INTEGER,
                doi TEXT UNIQUE,
                tag TEXT
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS 
            book (
                cite_key TEXT UNIQUE PRIMARY KEY,
                author TEXT,
                title TEXT,
                publisher TEXT,
                year INTEGER,
                doi TEXT UNIQUE,
                tag TEXT
            )
        """)
        db.commit()

        return db

    def run(self):
        db = self.connect_db()

        while True:
            self.io.write("\n\n==============================================\n"
                          "Kirjoita komento ja sen perään argumentit.\n"
                          "\nKäytettävissä olevat komennot: lisaa, hae, generoi\n"
                          "\nlisaa: lisaa <referenssityyppi> (esim. article, inproceedings, book)"
                          "\nlisaa: lisaa <DOI/URL> (esim. lisaa 10.1234/56789.1234)"
                          "\nhae: hae <attribuutti> <hakusana> (esim. hae author Matti)"
                          "\n\nSulje ohjelma : quit/exit")
            komento = self.io.read("> ")

            # Testausta varten, jotta ei jää ikuisesti silmukkaan
            if komento == "" and getattr(self, 'is_test_mode', False):
                break

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
                hakuattr = parts[1] if len(parts) > 1 else None
                hakusana = " ".join(parts[2:]) if len(parts) > 2 else ""

                haku = Hae(db, self.io, hakuattr, hakusana)
                haku.run()
                haku.tulosta()

            elif komento.startswith("generoi"):
                generoi = Generoi(db, self.io, self.output_dir)
                generoi.run()

        db.close()
