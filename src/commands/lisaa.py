class Lisaa:
    def __init__(self, arg, db, io):
        self.arg = arg
        self.db = db   
        self.io = io
        self.cursor = db.cursor()

    def run(self):
        # Tietojen kysyminen
        self.io.write("\n=== Add reference ===")

        cite_key = self.io.read("Cite (e.g. VPL11): ")

        if self.arg == "article":
            author = self.io.read("Author(s): ")
            title = self.io.read("Title: ")
            journal = self.io.read("Journal: ")
            year = self.io.read("Year: ")
            doi = self.io.read("DOI: ")

