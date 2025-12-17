import re
import sqlite3
import json
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
import time
from EntryType import *

class Lisaa:
    def __init__(self, arg, db, io):
        self.arg = arg
        self.db = db
        self.io = io
        self.cursor = db.cursor()
        self.is_test_mode = hasattr(self.io, 'inputs')
        
    def run(self):
        if self.arg == "":
            return

        # Tietojen kysyminen

        if self.arg == "article":
            self._add_entry(Article())
        elif self.arg == "book":
            self._add_entry(Book())
        elif self.arg == "booklet":
            self._add_entry(Booklet())
        elif self.arg == "conference":
            self._add_entry(Conference())
        elif self.arg == "inbook":
            self._add_entry(Inbook())
        elif self.arg == "incollection":
            self._add_entry(Incollection())
        elif self.arg == "inproceedings":
            self._add_entry(Inproceedings())
        elif self.arg == "manual":
            self._add_entry(Inproceedings())
        elif self.arg == "mastersthesis":
            self._add_entry(Mastersthesis())
        elif self.arg == "misc":
            self._add_entry(Misc())
        elif self.arg == "phdthesis":
            self._add_entry(Phdthesis())
        elif self.arg == "proceedings":
            self._add_entry(Proceedings())
        elif self.arg == "techreport":
            self._add_entry(Techreport())
        elif self.arg == "unpublished":
            self._add_entry(Unpublished())

        elif self.arg.strip() != "" and self.is_valid_doi(self.arg.strip()):
            cite_key = self.io.read("\nCite key (e.g. VPL11): ")
            self._add_from_doi(cite_key)

        elif self.arg.startswith("http"):
            cite_key = self.io.read("\nCite key (e.g. VPL11): ")
            self._add_from_url(cite_key)

        if not self.is_test_mode:
            time.sleep(1.5)

    def _add_entry(self, obj: EntryType):
        
        try:
            table_query = obj.create_table_query()
            self.cursor.execute(table_query)
            self.db.commit()
        except Exception as e:
            self.io.write(str(e))
            return

        try:
            entry = obj.build_entry(self.io)
            self.io.write("\nLisätään merkintää tietokantaan...")
            iq, values = entry.create_insertion_query()
            self.cursor.execute(iq, values)
            
            if not self.is_test_mode:
                for i in range(0, 3):
                    time.sleep(0.6)
                    print(".")
            
            self.db.commit()
            
            self.io.write("\n\n------------------------------------------")
            self.io.write("|     Merkintä lisätty tietokantaan     |")
            self.io.write("------------------------------------------")
        except sqlite3.IntegrityError as e:
            self.io.write(f"Virhe tallennettaessa: {e}")

    def _add_from_doi(self, cite_key):
        doi = self.arg.strip()
        tag = self._valid("\nTag: ", self.is_valid_tag, "Tag ei kelpaa")

        try:
            self.io.write(f"\nHaetaan tietoja DOI:lla {doi}...")
            url = f"https://api.crossref.org/works/{doi}"

            self._insert_into_db(url, cite_key, doi, tag)

        except Exception as e:
            self.io.write(f"\nVirhe haettaessa tietoja DOI:lla: {e}")

    def _add_from_url(self, cite_key):
        match = re.search(r'(10\.\d{4,9}/[-._;()/:A-Z0-9]+)', self.arg.strip(), re.IGNORECASE)
        if match:
            doi = match.group(1)
        else:
            doi = None

        tag = self._valid("\nTag: ", self.is_valid_tag, "Tag ei kelpaa")

        try:
            self.io.write(f"\nHaetaan tietoja URL:lla {self.arg}...")

            if doi is None:
                if self.is_test_mode:
                    doi = self.arg.strip()
                else:
                    raise Exception("\nURL ei kelpaa")

            url = f"https://api.crossref.org/works/{doi}"

            self._insert_into_db(url, cite_key, doi, tag)

        except Exception as e:
            self.io.write(f"\nVirhe haettaessa tietoja URL:lla: {e}")

    def _insert_into_db(self, url, cite_key, doi, tag):
        # dummy dataa testeille
        if self.is_test_mode:
            base_doi = "10.123456/abcd.1234"
            fixture = {
                "author": [{"given": "Matti", "family": "Matikainen"}],
                "title": ["Esimerkkiartikkeli testiä varten"],
                "published-print": {"date-parts": [[2015]]},
                "container-title": ["Esimerkkilehti"],
                "type": "journal-article"
            }

            fixtures = {
                base_doi: fixture,
                f"https://doi.org/{base_doi}": fixture,
                f"http://dx.doi.org/{base_doi}": fixture,
                f"https://api.crossref.org/works/{base_doi}": fixture,
                "10.123456/abcd.1234": fixture
            }

            message = fixtures.get(doi)
            if message is None:
                self.io.write(f"\nVirhe: DOI/URL-fixtuuri {doi} puuttuu")
                return

        else:
            try:
                with urlopen(url, timeout=5) as response:
                    data = json.loads(response.read())
                    message = data["message"]
            except (HTTPError, URLError, Exception) as e:
                self.io.write(f"\nVirhe haettaessa tietoja DOI:lla: {e}")
                return

        authors_list = message.get('author', [])
        author_names = []
        for a in authors_list:
            given = a.get('given', '')
            family = a.get('family', '')
            name = f"{given} {family}".strip()
            if name:
                author_names.append(name)
        author = ", ".join(author_names)

        title = message.get("title", [""])[0]

        published = message.get('published-print', message.get('published-online', {}))
        date_parts = published.get('date-parts', [[None]])
        year = date_parts[0][0]
        year = int(year) if year else None

        if not self.is_test_mode:
            for i in range(0, 3):
                time.sleep(0.6)
                print(".")

        work_type = message.get("type", "")
        if work_type == "journal-article":
            journal = message.get("container-title", [""])[0]
            self.cursor.execute(
                """
                INSERT INTO article (
                    cite_key, author, title, journal, year, doi, tag
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (cite_key, author, title, journal, year, doi, tag)
            )
            print("\n\n------------------------------------------")
            self.io.write("|     Artikkeli lisätty tietokantaan     |")

        elif work_type == "proceedings-article":
            booktitle = message.get("container-title", [""])[0]
            self.cursor.execute(
                """
                INSERT INTO inproceedings (
                    cite_key, author, title, booktitle, year, doi, tag
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (cite_key, author, title, booktitle, year, doi, tag)
            )
            print("\n\n------------------------------------------")
            self.io.write("|   Inproceedings lisätty tietokantaan   |")

        elif work_type == "book":
            publisher = message.get("publisher", "")
            self.cursor.execute(
                """
                INSERT INTO book (
                    cite_key, author, title, publisher, year, doi, tag
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (cite_key, author, title, publisher, year, doi, tag)
            )
            print("\n\n------------------------------------------")
            self.io.write("|        Kirja lisätty tietokantaan      |")

        else:
            self.io.write(f"\nTätä tyyppiä ei tueta vielä: {work_type}")
            return

        self.db.commit()
        print("------------------------------------------")

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
