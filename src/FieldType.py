from abc import ABC, abstractmethod
import re
from console_io import IO


class Author(str):
    err_msg = "Tekijä(t) ei kelpaa"
    
    def __new__(cls, value: str):
        value = value.strip() if value else ""
        if not cls.validate(value):
            raise ValueError(cls.err_msg)
        return str.__new__(cls, value)
    
    @staticmethod
    def validate(value: str) -> bool:
        # Sallitaan tekijän nimeen suomenkieliset kirjaimet, välilyönnit, pilkut ja yhdysviiva
        # Lisäksi voi olla useampi tekijä ','-merkillä eroteltuna.
        if not value or not value.strip():
            return False

        parts = [p.strip() for p in value.split(',')]
        pattern = r'^[a-zA-ZäöåÄÖÅ][a-zA-ZäöåÄÖÅ\-\s]*$'

        return all(re.match(pattern, p) for p in parts)
    

class Title(str):
    err_msg = "Otsikko ei kelpaa"

    def __new__(cls, value: str):
        value = value.strip() if value else ""
        if not cls.validate(value):
            raise ValueError(cls.err_msg)
        return str.__new__(cls, value)
    
    @staticmethod
    def validate(value: str) -> bool:
        # Otsikko ei voi olla tyhjä.
        return bool(value and value.strip())
    

class Journal(str):
    err_msg = "Julkaisupaikka ei kelpaa"
    
    def __new__(cls, value: str):
        value = value.strip() if value else ""
        if not cls.validate(value):
            raise ValueError(cls.err_msg)
        return str.__new__(cls, value)
    
    @staticmethod
    def validate(value: str) -> bool:
        # Lehden nimessä voi olla kirjaimia, numeroita, väliviivoja ja -lyöntejä.
        if not value or not value.strip():
            return False
        pattern = r'^[a-zA-ZäöåÄÖÅ0-9\-\s&.,\']+$'

        return bool(re.match(pattern, value.strip()))
    

class Year(int):
    err_msg = "Vuosi ei kelpaa"
    
    def __new__(cls, value):
        str_value = str(value).strip() if value is not None else ""
        if not cls.validate(str_value):
            raise ValueError(cls.err_msg)
        return int.__new__(cls, str_value)
    
    @staticmethod
    def validate(value: str) -> bool:
        # Vuosi voi olla 4-numeroinen luku välillä 1000-2999.
        if not value or not value.strip():
            return False
        pattern = r'^[12]\d{3}$'
        return bool(re.match(pattern, value.strip()))
    

class Doi(str):
    err_msg = "DOI ei kelpaa"
    
    def __new__(cls, value: str):
        value = value.strip() if value else ""
        if not cls.validate(value):
            raise ValueError(cls.err_msg)
        return str.__new__(cls, value)
    
    @staticmethod
    def validate(value: str) -> bool:
        # DOI voi olla tyhjä tai pätevä DOI-muoto
        if not value or not value.strip():
            return True
        pattern = r'^10\.\d{4,9}/[-._;()/:A-Z0-9]+$'
        return bool(re.match(pattern, value.strip(), re.IGNORECASE))
    

class Tag(str):
    err_msg = "Tag ei kelpaa"
    
    def __new__(cls, value: str):
        value = value.strip() if value else ""
        if not cls.validate(value):
            raise ValueError(cls.err_msg)
        return str.__new__(cls, value)
    
    @staticmethod
    def validate(value: str) -> bool:
        # Tag voi olla tyhjä.
        if not value or not value.strip():
            return True
        pattern = r'^[a-zA-ZäöåÄÖÅ0-9\-\s&.,\']+$'
        return bool(re.match(pattern, value.strip()))

class CiteKey(str):
    err_msg = "Cite key ei kelpaa"
    
    def __new__(cls, value: str):
        value = value.strip() if value else ""
        if not cls.validate(value):
            raise ValueError(cls.err_msg)
        return str.__new__(cls, value)
    
    @staticmethod
    def validate(value: str) -> bool:
        return True


#a = Year(1234)
#print(a)