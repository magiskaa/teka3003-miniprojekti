class Lisaa:
    def __init__(self, komento, arg, db, io):
        self.komento = komento
        self.arg = arg
        self.db = db   
        self.io = io
        self.cursor = db.cursor()

    def run(self):
        # Tietojen kysyminen
        self.io.write("\n=== Add reference ===")

        cite_key = self.io.read("Key (e.g. author2025): ")
        author = self.io.read("Author(s): ")
        title = self.io.read("Title: ")
        year = self.io.read("Year: ")