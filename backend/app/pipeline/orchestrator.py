from app.pipeline.stage_1_intent.extractor import extract_intent
from app.pipeline.stage_2_architect.architect import build_architecture

from app.pipeline.stage_3_schema.db_generator import generate_db_schema
from app.pipeline.stage_3_schema.api_generator import generate_api_schema
from app.pipeline.stage_3_schema.ui_generator import generate_ui_schema

from app.pipeline.stage_4_validation.cross_validator import validate_api_db_consistency
from app.pipeline.stage_4_validation.ui_api_validator import validate_ui_api

from app.pipeline.stage_5_repair.repair_engine import repair_api_schema

async def run_pipeline(user_prompt: str):

    intent = await extract_intent(user_prompt)

    architecture = await build_architecture(intent)

    db_schema = await generate_db_schema(intent)

    api_schema = await generate_api_schema(
        intent,
        db_schema
    )

    ui_schema = await generate_ui_schema(
        intent,
        api_schema
    )

    errors = []

    errors.extend(
        validate_api_db_consistency(
            api_schema,
            db_schema
        )
    )

    errors.extend(
        validate_ui_api(
            ui_schema,
            api_schema
        )
    )

    repaired = False

    if errors:
        api_schema = await repair_api_schema(
            errors,
            api_schema,
            db_schema
        )
        repaired = True

    return {
        "intent": intent.model_dump(),
        "architecture": architecture,
        "db_schema": db_schema.model_dump(),
        "api_schema": api_schema,
        "ui_schema": ui_schema.model_dump(),
        "errors": errors,
        "repaired": repaired
    }