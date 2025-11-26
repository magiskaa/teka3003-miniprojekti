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
            author = self.io.read("Author(s): ")
            author_validi = self.validate_author(author)
            while author_validi:
                author = self.io.read("Author(s): ")
                author_validi = self.validate_author(author)
            title = self.io.read("Title: ")
            journal = self.io.read("Journal: ")
            year = self.io.read("Year: ")
            doi = self.io.read("DOI: ")

            self.io.write("\nArticle citation added")

    def validate_author(self, text):
        if not re.match('^[a-zA-ZäöåÄÖÅ]+$', text):
            self.io.write("Ei validi nimi tekijälle")
            return True
        return False