from jsonschema import validate


def assert_valid_schema(j_response):
    schema = {
        "type": "object",
        "properties": {
            "userId": {"type": "number"},
            "id": {"type": "number"},
            "title": {"type": "string"},
            "body": {"type": "string"},
        },
    }

    return validate(instance=j_response, schema=schema)

