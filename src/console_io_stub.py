class IOStub:
    def __init__(self, inputs=None):
        self.inputs = inputs or []
        self.outputs = []

    def write(self, text):
        self.outputs.append(text)
        
    def read(self, prompt):
        if len(self.inputs) > 0:
            return self.inputs.pop(0)
        else:
            return ""
        
    def add_input(self, input):
        self.inputs.append(input)