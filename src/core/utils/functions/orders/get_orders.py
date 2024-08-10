import json

from core.utils.functions.total.fetch_temp import fetch_temp
from core.utils.functions.total.fetch_total import fetch_total

async def get_orders(file_path: str = None,
                     file_name: str = None) -> str:
    
    with open(f'{file_path}/{file_name}') as file:
        data = json.load(file)
        
        orders = data['orders']
        max_length = max(len(order['phone_number']) for order in orders)
        
        output = []
        for index, order in enumerate(orders, start=1):
            output.append(f"{index}: {order['phone_number'].ljust(max_length)} | {order['count']}")
        
        output.append("-----------------")
        output.append(f"Было: {await fetch_total(file_path, file_name)} | Текущее: {await fetch_temp(file_path, file_name)}")
        
        return "\n".join(output)