import json

async def delete_order(file_path: str = None, file_name: str = None, ids: str = None) -> None:
    ids_list = [int(i.strip()) - 1 for i in ids.replace(',', ' ').split()]

    with open(f'{file_path}/{file_name}') as file:
        data = json.load(file)

    ids_list.sort(reverse=True)
    
    for idx in ids_list:
        if 0 <= idx < len(data['orders']):
            data['orders'].pop(idx)

    with open(f"{file_path}/{file_name}", "w") as file:
        json.dump(data, file)