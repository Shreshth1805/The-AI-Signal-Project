from pydantic import BaseModel
from typing import List

class Column(BaseModel):
    name: str
    type: str

class Table(BaseModel):
    name: str
    columns: List[Column]

class DBSchema(BaseModel):
    tables: List[Table]