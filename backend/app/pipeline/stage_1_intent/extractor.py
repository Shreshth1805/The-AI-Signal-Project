from app.llm.structured_generation import generate_json
from app.schemas.intent_schema import IntentSchema

async def extract_intent(user_prompt: str):

    prompt = f'''
    Extract app intent.

    User Prompt:
    {user_prompt}

    Return valid JSON:
    {{
      "app_name": "",
      "app_type": "",
      "features": [],
      "roles": []
    }}
    '''

    result = await generate_json(prompt)

    return IntentSchema(**result)