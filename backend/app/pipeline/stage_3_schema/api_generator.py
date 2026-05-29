from app.schemas.api_schema import APISchema
from app.llm.structured_generation import generate_json

async def generate_api_schema(intent, db_schema):

    prompt = f'''
    Generate API schema.

    Intent:
    {intent.model_dump_json()}

    DB:
    {db_schema.model_dump_json()}
    '''

    result = await generate_json(prompt)

    return APISchema(**result)