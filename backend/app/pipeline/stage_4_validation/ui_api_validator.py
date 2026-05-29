def validate_ui_api(ui_schema, api_schema):

    errors = []

    api_paths = [
        e.path
        for e in api_schema.endpoints
    ]

    for page in ui_schema.pages:

        for component in page.components:

            api = component.props.get("api")

            if api and api not in api_paths:
                errors.append(
                    f"Missing API reference {api}"
                )

    return errors