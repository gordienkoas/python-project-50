import json


def render_json(lst):
    return json.dumps(lst, indent=4)