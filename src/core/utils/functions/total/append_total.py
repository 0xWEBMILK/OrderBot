import json

async def append_total(file_path: str = None, file_name: str = None, total: str = 0) -> None:
    with open(f'{file_path}/{file_name}') as file:
        data = json.load(file)
        data['total'] = total
        data['temp'] = data['total']

    with open(f"{file_path}/{file_name}", "w") as file:
        json.dump(data, file)