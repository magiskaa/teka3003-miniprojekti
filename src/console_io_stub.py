class IOStub:
    def __init__(self, inputs=None):
        self.inputs = inputs or []
        self.outputs = []

    def write(self, text):
        self.outputs.append(text)

    def read(self, prompt):
        if len(self.inputs) > 0:
            return self.inputs.pop(0)
        return ""

    def add_input(self, text):
        self.inputs.append(text)
