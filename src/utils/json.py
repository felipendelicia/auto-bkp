import json

def import_json(src:str):
    with open(src) as file:
        json_file = json.load(file)

    return json_file
