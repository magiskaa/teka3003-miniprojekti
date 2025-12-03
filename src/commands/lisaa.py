import re
import sqlite3
class Lisaa:
    def __init__(self, arg, db, io):
        self.arg = arg
        self.db = db
        self.io = io
        self.cursor = db.cursor()

    def run(self):
        # Tietojen kysyminen
        cite_key = self.io.read("\nCite key (e.g. VPL11): ")

        if self.arg == "article":
            author = self._valid("\nAuthor(s): ", self.is_valid_author, "Tekijä(t) ei kelpaa")
            title = self._valid("\nTitle: ", self.is_valid_title, "Otsikko ei kelpaa")
            journal = self._valid("\nJournal: ", self.is_valid_journal, "Julkaisupaikka ei kelpaa")
            year = self._valid("\nYear: ", self.is_valid_year, "Vuosi ei kelpaa")
            doi = self._valid("\nDOI: ", self.is_valid_doi, "DOI ei kelpaa")
            tag = self._valid("\nTag: ", self.is_valid_tag, "Tag ei kelpaa")

            try:
                doi_value = doi.strip() if doi and doi.strip() else None
                self.cursor.execute(
                    """
                    INSERT INTO article (cite_key, author, title, journal, year, doi, tag)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,
                    (cite_key, author, title, journal, int(year), doi_value, tag)
                )
                self.db.commit()

                print("\n\n------------------------------------------")
                self.io.write("|     Artikkeli lisätty tietokantaan     |")
                print("------------------------------------------")
            except sqlite3.IntegrityError as e:
                self.io.write(f"Virhe tallennettaessa: {e}")

    def _valid(self, syote, validator, error_message):
        # Yleinen valid tarkistin
        while True:
            arvo = self.io.read(syote)
            if validator(arvo):
                return arvo
            self.io.write(error_message)

    def is_valid_author(self, text):
        # Sallitaan tekijän nimeen suomenkieliset kirjaimet, välilyönnit, pilkut ja yhdysviiva
        # Lisäksi voi olla useampi tekijä ','-merkillä eroteltuna.
        if not text or not text.strip():
            return False

        parts = [p.strip() for p in text.split(',')]
        pattern = r'^[a-zA-ZäöåÄÖÅ][a-zA-ZäöåÄÖÅ\-\s]*$'

        return all(re.match(pattern, p) for p in parts)

    def is_valid_title(self, text):
        # Otsikko ei voi olla tyhjä.
        return bool(text and text.strip())

    def is_valid_journal(self, text):
        # Lehden nimessä voi olla kirjaimia, numeroita, väliviivoja ja -lyöntejä.
        if not text or not text.strip():
            return False
        pattern = r'^[a-zA-ZäöåÄÖÅ0-9\-\s&.,\']+$'

        return bool(re.match(pattern, text.strip()))

    def is_valid_year(self, text):
        # Vuosi voi olla 4-numeroinen luku välillä 1000-2999.
        if not text or not text.strip():
            return False
        pattern = r'^[12]\d{3}$'
        return bool(re.match(pattern, text.strip()))

    def is_valid_doi(self, text):
        # DOI voi olla tyhjä tai pätevä DOI-muoto
        if not text or not text.strip():
            return True
        pattern = r'^10\.\d{4,9}/[-._;()/:A-Z0-9]+$'
        return bool(re.match(pattern, text.strip(), re.IGNORECASE))
    
    def is_valid_tag(self, text):
        # Tag voi olla tyhjä.
        if not text or not text.strip():
            return True
        pattern = r'^[a-zA-ZäöåÄÖÅ0-9\-\s&.,\']+$'
        return bool(re.match(pattern, text.strip()))
