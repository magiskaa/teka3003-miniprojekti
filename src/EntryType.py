from dataclasses import dataclass, fields, field, asdict
from abc import ABC
from typing import Optional, get_origin, get_args, Union
from FieldType import *

@dataclass
class EntryType(ABC):

    cite_key: Optional[CiteKey] = field(default=None, metadata={"prompt": "Cite key (e.g. VPL11)", "required": True})


    @classmethod
    def _unwrap_optional(cls, t):
        origin = get_origin(t)
        if origin is Union:
            args = [a for a in get_args(t) if a is not type(None)]
            return args[0] if args else str
        return t


    @classmethod
    def create_table_query(cls):
        table = cls.__name__.lower()
        columns = []

        for f in fields(cls):
            py_type = cls._unwrap_optional(f.type)
            sql_type = cls.python_type_to_sqlite(py_type, "TEXT")

            columns.append(f"{f.name} {sql_type}" + (" UNIQUE PRIMARY KEY" if f.name == "cite_key" else ""))

        return f"CREATE TABLE IF NOT EXISTS {table} ({', '.join(columns)});"


    def create_insertion_query(self):
        table = self.__class__.__name__.lower()
        fields_names = [f.name for f in fields(self.__class__)]
        values = list(asdict(self).values())

        return f"INSERT INTO {table} ({', '.join(fields_names)}) VALUES ({', '.join('?' for _ in values)});", values


    @classmethod
    def build_entry(cls, io):
        obj = cls()

        for f in fields(cls):
            meta = f.metadata
            prompt = meta.get("prompt")
            if not prompt:
                continue

            required = meta.get("required", False)
            value_type = cls._unwrap_optional(f.type)

            while True:
                val = io.read(f"\n{prompt}{' (optional)' if not required else ''}: ")

                if not val and not required:
                    setattr(obj, f.name, None)
                    break

                try:
                    setattr(obj, f.name, value_type(val))
                    break
                except Exception as e:
                    io.write(str(e))

        return obj
    
    @staticmethod
    def python_type_to_sqlite(t, backup="TEXT"):
        if issubclass(t, int):
            return "INTEGER"
        if issubclass(t, str):
            return "TEXT"
        if issubclass(t, float):
            return "REAL"
        if issubclass(t, bool):
            return "INTEGER"
        return backup

#-------------------Dataclasses-----------------------------------------
#TODO: Add missing optional fields

@dataclass
class Article(EntryType):
    author: Optional[Author] = field(default=None, metadata={"prompt": "Author", "required": True})
    title: Optional[Title] = field(default=None, metadata={"prompt": "Title", "required": True})
    journal: Optional[Journal] = field(default=None, metadata={"prompt": "Journal", "required": True})
    year: Optional[Year] = field(default=None, metadata={"prompt": "Year", "required": True})
    
    volume: Optional[str] = field(default=None, metadata={"prompt": "Volume"})
    number: Optional[str] = field(default=None, metadata={"prompt": "Number"})
    pages: Optional[str] = field(default=None, metadata={"prompt": "Pages"})
    
    doi: Optional[Doi] = field(default=None, metadata={"prompt": "DOI", "required": True})
    tag: Optional[Tag] = field(default=None, metadata={"prompt": "Tag"})


@dataclass
class Book(EntryType):
    author: Optional[Author] = field(default=None, metadata={"prompt": "Author", "required": True})
    title: Optional[str] = field(default=None, metadata={"prompt": "Title", "required": True})
    publisher: Optional[str] = field(default=None, metadata={"prompt": "Publisher", "required": True})
    address: Optional[str] = field(default=None, metadata={"prompt": "Address", "required": True})
    year: Optional[str] = field(default=None, metadata={"prompt": "Year", "required": True})

    doi: Optional[Doi] = field(default=None, metadata={"prompt": "DOI", "required": True})
    tag: Optional[Tag] = field(default=None, metadata={"prompt": "Tag"})

@dataclass
class Booklet(EntryType):
    title: Optional[str] = field(default=None, metadata={"prompt": "Title", "required": True})
    author: Optional[str] = field(default=None, metadata={"prompt": "Author", "required": True})
    howpublished: Optional[str] = field(default=None, metadata={"prompt": "Howpublished", "required": True})
    month: Optional[str] = field(default=None, metadata={"prompt": "Month", "required": True})
    year: Optional[str] = field(default=None, metadata={"prompt": "Year", "required": True})
    
    editor: Optional[str] = field(default=None, metadata={"prompt": "Editor"})
    volume: Optional[str] = field(default=None, metadata={"prompt": "Volume"})
    number: Optional[str] = field(default=None, metadata={"prompt": "Number"})
    series: Optional[str] = field(default=None, metadata={"prompt": "Series"})
    organization: Optional[str] = field(default=None, metadata={"prompt": "Organization"})
    month: Optional[str] = field(default=None, metadata={"prompt": "Month"})
    note: Optional[str] = field(default=None, metadata={"prompt": "Note"})

    doi: Optional[Doi] = field(default=None, metadata={"prompt": "DOI", "required": True})
    tag: Optional[Tag] = field(default=None, metadata={"prompt": "Tag"})

@dataclass
class Conference(EntryType):
    author: Optional[str] = field(default=None, metadata={"prompt": "Author", "required": True})
    title: Optional[str] = field(default=None, metadata={"prompt": "Title", "required": True})
    booktitle: Optional[str] = field(default=None, metadata={"prompt": "Booktitle", "required": True})
    year: Optional[str] = field(default=None, metadata={"prompt": "Year", "required": True})
    
    series: Optional[str] = field(default=None, metadata={"prompt": "Series"})
    pages: Optional[str] = field(default=None, metadata={"prompt": "Pages"})
    publisher: Optional[str] = field(default=None, metadata={"prompt": "Publisher"})
    address: Optional[str] = field(default=None, metadata={"prompt": "Address"})

    doi: Optional[Doi] = field(default=None, metadata={"prompt": "DOI", "required": True})
    tag: Optional[Tag] = field(default=None, metadata={"prompt": "Tag"})

@dataclass
class Inbook(EntryType):
    author: Optional[str] = field(default=None, metadata={"prompt": "Author", "required": True})
    title: Optional[str] = field(default=None, metadata={"prompt": "Title", "required": True})
    booktitle: Optional[str] = field(default=None, metadata={"prompt": "Booktitle", "required": True})
    publisher: Optional[str] = field(default=None, metadata={"prompt": "Publisher", "required": True})
    year: Optional[str] = field(default=None, metadata={"prompt": "Year", "required": True})
    
    address: Optional[str] = field(default=None, metadata={"prompt": "Address"})
    pages: Optional[str] = field(default=None, metadata={"prompt": "Pages"})

    doi: Optional[Doi] = field(default=None, metadata={"prompt": "DOI", "required": True})
    tag: Optional[Tag] = field(default=None, metadata={"prompt": "Tag"})

@dataclass
class Incollection(EntryType):
    author: Optional[str] = field(default=None, metadata={"prompt": "Author", "required": True})
    title: Optional[str] = field(default=None, metadata={"prompt": "Title", "required": True})
    booktitle: Optional[str] = field(default=None, metadata={"prompt": "Booktitle", "required": True})
    publisher: Optional[str] = field(default=None, metadata={"prompt": "Publisher", "required": True})
    year: Optional[str] = field(default=None, metadata={"prompt": "Year", "required": True})
    
    editor: Optional[str] = field(default=None, metadata={"prompt": "Editor"})
    address: Optional[str] = field(default=None, metadata={"prompt": "Address"})
    pages: Optional[str] = field(default=None, metadata={"prompt": "Pages"})

    doi: Optional[Doi] = field(default=None, metadata={"prompt": "DOI", "required": True})
    tag: Optional[Tag] = field(default=None, metadata={"prompt": "Tag"})

@dataclass
class Inproceedings(EntryType):
    author: Optional[str] = field(default=None, metadata={"prompt": "Author", "required": True})
    title: Optional[str] = field(default=None, metadata={"prompt": "Title", "required": True})
    booktitle: Optional[str] = field(default=None, metadata={"prompt": "Booktitle", "required": True})
    year: Optional[str] = field(default=None, metadata={"prompt": "Year", "required": True})
    
    series: Optional[str] = field(default=None, metadata={"prompt": "Series"})
    pages: Optional[str] = field(default=None, metadata={"prompt": "Pages"})
    publisher: Optional[str] = field(default=None, metadata={"prompt": "Publisher"})
    address: Optional[str] = field(default=None, metadata={"prompt": "Address"})

    doi: Optional[Doi] = field(default=None, metadata={"prompt": "DOI", "required": True})
    tag: Optional[Tag] = field(default=None, metadata={"prompt": "Tag"})

@dataclass
class Manual(EntryType):
    title: Optional[str] = field(default=None, metadata={"prompt": "Title", "required": True})
    year: Optional[str] = field(default=None, metadata={"prompt": "Year", "required": True})
    
    author: Optional[str] = field(default=None, metadata={"prompt": "Author"})
    organization: Optional[str] = field(default=None, metadata={"prompt": "Organization"})
    address: Optional[str] = field(default=None, metadata={"prompt": "Address"})

    doi: Optional[Doi] = field(default=None, metadata={"prompt": "DOI", "required": True})
    tag: Optional[Tag] = field(default=None, metadata={"prompt": "Tag"})

@dataclass
class Mastersthesis(EntryType):
    author: Optional[str] = field(default=None, metadata={"prompt": "Author", "required": True})
    title: Optional[str] = field(default=None, metadata={"prompt": "Title", "required": True})
    school: Optional[str] = field(default=None, metadata={"prompt": "School", "required": True})
    year: Optional[str] = field(default=None, metadata={"prompt": "Year", "required": True})
    
    address: Optional[str] = field(default=None, metadata={"prompt": "Address"})
    month: Optional[str] = field(default=None, metadata={"prompt": "Month"})

    doi: Optional[Doi] = field(default=None, metadata={"prompt": "DOI", "required": True})
    tag: Optional[Tag] = field(default=None, metadata={"prompt": "Tag"})

@dataclass
class Misc(EntryType):
    title: Optional[str] = field(default=None, metadata={"prompt": "Title", "required": True})
    
    year: Optional[str] = field(default=None, metadata={"prompt": "Year"})
    author: Optional[str] = field(default=None, metadata={"prompt": "Author"})
    howpublished: Optional[str] = field(default=None, metadata={"prompt": "Howpublished"})
    note: Optional[str] = field(default=None, metadata={"prompt": "Note"})

    doi: Optional[Doi] = field(default=None, metadata={"prompt": "DOI", "required": True})
    tag: Optional[Tag] = field(default=None, metadata={"prompt": "Tag"})

@dataclass
class Phdthesis(EntryType):
    author: Optional[str] = field(default=None, metadata={"prompt": "Author", "required": True})
    title: Optional[str] = field(default=None, metadata={"prompt": "Title", "required": True})
    school: Optional[str] = field(default=None, metadata={"prompt": "School", "required": True})
    year: Optional[str] = field(default=None, metadata={"prompt": "Year", "required": True})
    
    address: Optional[str] = field(default=None, metadata={"prompt": "Address"})
    month: Optional[str] = field(default=None, metadata={"prompt": "Month"})

    doi: Optional[Doi] = field(default=None, metadata={"prompt": "DOI", "required": True})
    tag: Optional[Tag] = field(default=None, metadata={"prompt": "Tag"})

@dataclass
class Proceedings(EntryType):
    title: Optional[str] = field(default=None, metadata={"prompt": "Title", "required": True})
    year: Optional[str] = field(default=None, metadata={"prompt": "Year", "required": True})
    
    editor: Optional[str] = field(default=None, metadata={"prompt": "Editor"})
    series: Optional[str] = field(default=None, metadata={"prompt": "Series"})
    volume: Optional[str] = field(default=None, metadata={"prompt": "Volume"})
    publisher: Optional[str] = field(default=None, metadata={"prompt": "Publisher"})
    address: Optional[str] = field(default=None, metadata={"prompt": "Address"})

    doi: Optional[Doi] = field(default=None, metadata={"prompt": "DOI", "required": True})
    tag: Optional[Tag] = field(default=None, metadata={"prompt": "Tag"})

@dataclass
class Techreport(EntryType):
    author: Optional[str] = field(default=None, metadata={"prompt": "Author", "required": True})
    title: Optional[str] = field(default=None, metadata={"prompt": "Title", "required": True})
    institution: Optional[str] = field(default=None, metadata={"prompt": "Institution", "required": True})
    year: Optional[str] = field(default=None, metadata={"prompt": "Year", "required": True})
    number: Optional[str] = field(default=None, metadata={"prompt": "Number", "required": True})
    
    address: Optional[str] = field(default=None, metadata={"prompt": "Address"})
    month: Optional[str] = field(default=None, metadata={"prompt": "Month"})

    doi: Optional[Doi] = field(default=None, metadata={"prompt": "DOI", "required": True})
    tag: Optional[Tag] = field(default=None, metadata={"prompt": "Tag"})

@dataclass
class Unpublished(EntryType):
    author: Optional[str] = field(default=None, metadata={"prompt": "Author", "required": True})
    title: Optional[str] = field(default=None, metadata={"prompt": "Title", "required": True})
    year: Optional[str] = field(default=None, metadata={"prompt": "Year", "required": True})

    doi: Optional[Doi] = field(default=None, metadata={"prompt": "DOI", "required": True})
    tag: Optional[Tag] = field(default=None, metadata={"prompt": "Tag"})

#try:
#    io = IO()
#    a = Article()
#    c=a.create_table_query()
#    print(c)
#    b=a.build_entry(io)
#    print(b)
#    x=b.create_insertion_query()
#    print(x)
#except ValueError as e:
#    print(e)


