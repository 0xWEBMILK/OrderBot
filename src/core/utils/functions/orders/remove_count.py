import json

async def remove_count(file_path: str = None, file_name: str = None, total: str = 0) -> None:
    with open(f'{file_path}/{file_name}') as file:
        data = json.load(file)
        data['temp'] = int(data['temp']) - int(total)

    with open(f"{file_path}/{file_name}", "w") as file:
        json.dump(data, file)