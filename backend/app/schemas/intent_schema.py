from pydantic import BaseModel
from typing import List

class Feature(BaseModel):
    name: str
    description: str

class IntentSchema(BaseModel):
    app_name: str
    app_type: str
    features: List[Feature]
    roles: List[str]