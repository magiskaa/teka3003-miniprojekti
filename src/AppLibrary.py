from app import App
from console_io_stub import IOStub

class AppLibrary:
    def __init__(self):
        self._io = IOStub()
        self._app = App(self._io, db_name=":memory:")

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

            expected_tables = ['articles', 'inproceedings', 'books']
            for table in expected_tables:
                if table not in tables:
                    raise AssertionError(f"Taulu '{table}' puuttuu tietokannasta")

            self._io.write("Yhdistetty tietokantaan")

            db.close()
        except Exception as e:
            raise AssertionError(f"Tietokantaan yhdistäminen epäonnistui: {str(e)}") from e
