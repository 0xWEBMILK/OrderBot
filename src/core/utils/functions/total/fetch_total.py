import json

async def fetch_total(file_path: str = None, file_name: str = None) -> str:
    with open(f'{file_path}/{file_name}') as file:
        return json.load(file)['total']