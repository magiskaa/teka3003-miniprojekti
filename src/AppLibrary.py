from app import App
from console_io_stub import IOStub

class AppLibrary:
    def __init__(self):
        self._io = IOStub()
        self._app = App(self._io)

    def input(self, input):
        self._io.add_input(input)

    def output_should_contain(self, text):
        for output in self._io.outputs:
            if text in output:
                return
        raise AssertionError(f"Output \"{text}\" is not in {self._io.outputs}")

    def run_application(self):
        self._app.run()
