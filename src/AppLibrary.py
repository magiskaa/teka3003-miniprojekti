import os
from app import App
from console_io_stub import IOStub

class AppLibrary:
    def __init__(self):
        self._io = IOStub()
        self.output_dir = "robot_output"
        os.makedirs(self.output_dir, exist_ok=True)
        self._app = App(self._io, db_name=":memory:", output_dir=self.output_dir)

    def input(self, text):
        self._io.add_input(text)

    def output_should_contain(self, text):
        for output in self._io.outputs:
            if text in output:
                return
        raise AssertionError(f"Output \"{text}\" is not in {self._io.outputs}")

    def run_application(self):
        self._app.run()

    def check_database_connection(self):
        try:
            db = self._app.connect_db()
            cursor = db.cursor()

            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            rows = cursor.fetchall()
            tables = [row['name'] for row in rows]

            expected_tables = ['article', 'inproceedings', 'book']
            for table in expected_tables:
                if table not in tables:
                    raise AssertionError(f"Taulu '{table}' puuttuu tietokannasta")

            self._io.write("Yhdistetty tietokantaan")

            db.close()
        except Exception as e:
            raise AssertionError(f"Tietokantaan yhdistäminen epäonnistui: {str(e)}") from e

    def check_generated_file_exists(self):
        path = os.path.join(self.output_dir, "lahteet.bib")
        if not os.path.isfile(path):
            raise AssertionError("BibTeX-tiedostoa ei luotu onnistuneesti")
        return path

    def read_generated_file(self):
        path = self.check_generated_file_exists()
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    def file_should_contain(self, text):
        content = self.read_generated_file()
        if text not in content:
            raise AssertionError(f"Teksti {text} ei löytynyt tiedostosta.\nSisältö oli {content}")
