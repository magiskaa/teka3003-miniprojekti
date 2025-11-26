import re
class Lisaa:
    def __init__(self, arg, db, io):
        self.arg = arg
        self.db = db   
        self.io = io
        self.cursor = db.cursor()

    def run(self):
        # Tietojen kysyminen
        cite_key = self.io.read("Cite (e.g. VPL11): ")

        if self.arg == "article":
            author = self._valid("Author(s): ", self.is_valid_author, "Ei validi nimi tekijälle")
            title = self.io.read("Title: ")
            journal = self.io.read("Journal: ")
            year = self.io.read("Year: ")
            doi = self.io.read("DOI: ")

            self.io.write("\nArticle citation added")

    def _valid(self, syote, validator, error_message):
        # Yleinen valid tarkistin
        while True:
            arvo = self.io.read(syote)
            if validator(arvo):
                return arvo
            self.io.write(error_message)

    def is_valid_author(self, text):
        # Sallitaan suomenkieliset kirjaimet, välilyönnit, pilkut ja yhdysviiva
        # Lisäksi voi olla useampi tekijä ','-merkillä eroteltuna.
        if not text or not text.strip():
            return False

        parts = [p.strip() for p in text.split(',')]
        pattern = r'^[a-zA-ZäöåÄÖÅ][a-zA-ZäöåÄÖÅ\-\s]*$'

        return all(re.match(pattern, p) for p in parts)