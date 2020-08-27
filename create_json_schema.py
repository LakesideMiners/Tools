"""Create a json schema.
With input data:
{'returnUrl': 'http://example.com'}

Example result:
{
    "required": [
        "returnUrl"
    ],
    "type": "object",
    "description": "TODO",
    "properties": {
        "returnUrl": {
            "type": "string",
            "example": "http://example.com",
            "description": "TODO"
        }
    }
}

"""
import json
# Edit this as the input data.
data = {'returnUrl': 'http://example.com'}


def create_schema(val):
    """
    Create a valid json schema from a dictionary of example data.
    It assumes all values are required.

    Recursive json schema creator from data.
    :param val:
    :return:
    """
    if val is None:  # Assume string.
        return {
            'type': 'string',
            'example': "",
            'description': "TODO",
        }
    if type(val) is int:
        return {
            'type': 'integer',
            'example': val,
            'description': "TODO",
        }
    if type(val) is str:
        return {
            'type': 'string',
            'example': val,
            'description': "TODO",
        }
    if type(val) is list or type(val) is tuple:
        return {
            'type': 'array',
            'items': create_schema(val[0])
        }
    if type(val) is dict:
        properties = {k: create_schema(v) for k, v in val.items()}
        return {
            "type": "object",
            'description': "TODO",
            "required": val.keys(),
            "properties": properties,
        }
    print("Unknown???", val)


print(json.dumps(create_schema(data), indent=4))
