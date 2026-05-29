from app.llm.structured_generation import generate_json

async def repair_api_schema(errors, api_schema, db_schema):

    prompt = f'''
    Repair API schema.

    Errors:
    {errors}

    Existing API:
    {api_schema.model_dump_json()}

    DB:
    {db_schema.model_dump_json()}
    '''

    return await generate_json(prompt)