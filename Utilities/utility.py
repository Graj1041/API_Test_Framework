import jsonschema
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

    try:
        validate(instance=j_response, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True


