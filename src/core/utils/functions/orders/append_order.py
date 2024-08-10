import json


async def append_order(
        file_path: str = None,
        file_name: str = None,
        phone_number: str = None,
        count: str = None) -> None:

    with open(f'{file_path}/{file_name}') as file:
        data = json.load(file)
        data['orders'].append({"phone_number": phone_number, "count": count})

    with open(f"{file_path}/{file_name}", "w") as file:
        json.dump(data, file)