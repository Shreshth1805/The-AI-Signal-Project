from app.schemas.ui_schema import UISchema
from app.llm.structured_generation import generate_json

async def generate_ui_schema(intent, api_schema):

    prompt = f'''
    Generate UI schema.

    Intent:
    {intent.model_dump_json()}

    API:
    {api_schema.model_dump_json()}
    '''

    result = await generate_json(prompt)

    return UISchema(**result)