def validate_api_db_consistency(api_schema, db_schema):

    errors = []

    db_tables = [
        t.name.lower()
        for t in db_schema.tables
    ]

    for endpoint in api_schema.endpoints:

        matched = False

        for table in db_tables:
            if table in endpoint.path.lower():
                matched = True

        if not matched:
            errors.append(
                f"Endpoint {endpoint.path} has no DB mapping"
            )

    return errors