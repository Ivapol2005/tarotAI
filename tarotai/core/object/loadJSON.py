import json
from pathlib import Path

def load_JSON_data(filename):
    # filename_json_spreads = 'spreads.json'

    folder_core = Path(__file__).parent
    folder_data = folder_core.parent.parent / "data"
    target_file = folder_data / filename

    if not target_file.exists():
        raise FileNotFoundError(f"JSON file not found at {target_file}")

    with open(target_file, 'r') as file:
        json_return = json.load(file)

    return json_return
    # spreads_list = json_spreads["spreads"]
