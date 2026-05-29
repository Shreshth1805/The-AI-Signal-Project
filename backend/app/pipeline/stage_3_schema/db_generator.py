from app.schemas.db_schema import DBSchema
from app.llm.structured_generation import generate_json

async def generate_db_schema(intent):

    prompt = f'''
    Generate DB schema.

    Intent:
    {intent.model_dump_json()}
    '''

    result = await generate_json(prompt)

    return DBSchema(**result)