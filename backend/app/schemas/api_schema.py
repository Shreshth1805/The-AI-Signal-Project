from pydantic import BaseModel
from typing import List

class Endpoint(BaseModel):
    path: str
    method: str
    request_model: dict
    response_model: dict

class APISchema(BaseModel):
    endpoints: List[Endpoint]