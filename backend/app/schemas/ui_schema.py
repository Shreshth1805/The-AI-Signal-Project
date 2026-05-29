from pydantic import BaseModel
from typing import List

class Component(BaseModel):
    type: str
    props: dict

class Page(BaseModel):
    name: str
    route: str
    components: List[Component]

class UISchema(BaseModel):
    pages: List[Page]