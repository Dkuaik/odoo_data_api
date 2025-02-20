import json
from pathlib import Path

def load_json_from_raw(file_path: str) -> dict:

    # Generation of the path to load the file
    project_dir = Path(__file__).resolve().parents[2]
    relative_path = f'data/raw/{file_path}'
    file_path = project_dir / relative_path

    # Loading the leads from a json file
    with open(file_path, 'r') as file:
        data = json.load(file)

    if data:
        return data
    else:
        raise ValueError(f"File {file_path} is empty")

def load_json_from_processed(file_path: str) -> dict:

    # Generation of the path to load the file
    project_dir = Path(__file__).resolve().parents[2]
    relative_path = f'data/processed/{file_path}'
    file_path = project_dir / relative_path

    # Loading the leads from a json file
    with open(file_path, 'r') as file:
        data = json.load(file)

    if data:
        return data
    else:
        raise ValueError(f"File {file_path} is empty")
    
def save_json_to_raw(data: dict, file_path: str) -> None:
    
    # Generation of the path to save the file
    project_dir = Path(__file__).resolve().parents[2]
    relative_path = f'data/raw/{file_path}'
    file_path = project_dir / relative_path

    # Saving the leads to a json file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def save_json_to_processed(data: dict, file_path: str) -> None:
    
    # Generation of the path to save the file
    project_dir = Path(__file__).resolve().parents[2]
    relative_path = f'data/processed/{file_path}'
    file_path = project_dir / relative_path

    # Saving the leads to a json file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)