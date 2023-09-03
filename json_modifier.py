import json

def flatten_json(json_obj, parent_key='', separator='__'):
    items = []
    for key, value in json_obj.items():
        new_key = parent_key + separator + key if parent_key else key
        if isinstance(value, dict):
            items.extend(flatten_json(value, new_key, separator=separator).items())
        else:
            items.append((new_key, value))
    return dict(items)

def process_json(input_file, output_file):
    with open(input_file, 'r') as f:
        data = json.load(f)

    flat_data = flatten_json(data)
    result = [{"name": key, "value": value, "slotSetting": False} for key, value in flat_data.items()]

    with open(output_file, 'w') as f:
        json.dump(result, f, indent=2)

if __name__ == "__main__":
    input_file = "input.json"
    output_file = "result.json"
    process_json(input_file, output_file)
