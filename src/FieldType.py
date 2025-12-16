from abc import ABC, abstractmethod
import re
from console_io import IO


class FieldType(ABC):
    
    @abstractmethod
    def ask_field(self, io, msg):
        while True:
            val = io.read(msg)
            if self.validate(val):
                return val
            
            io.write(self.err_msg)

    @abstractmethod
    def validate(self, value):
        pass

class Author(FieldType):
    def __init__(self, io):
        super().__init__()
        self.err_msg = "Tekijä(t) ei kelpaa"
        self.value = self.ask_field(io)

    def ask_field(self, io):
        return super().ask_field(io, "\nAuthor(s): ")
    
    def validate(self, value):
        # Sallitaan tekijän nimeen suomenkieliset kirjaimet, välilyönnit, pilkut ja yhdysviiva
        # Lisäksi voi olla useampi tekijä ','-merkillä eroteltuna.
        if not value or not value.strip():
            return False

        parts = [p.strip() for p in value.split(',')]
        pattern = r'^[a-zA-ZäöåÄÖÅ][a-zA-ZäöåÄÖÅ\-\s]*$'

        return all(re.match(pattern, p) for p in parts)
    

io = IO()
a = Author(io)
print(a.value)