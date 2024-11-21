# main.py

from item import ItemFactory, SmallItem, HeavyItem, RefrigeratedItem, LiquidItem
from container import Container
from ship import Ship
from port import Port
import json

input_file = 'input.json'
output_file = 'output.json'

# Відкриваємо і читаємо JSON файл
with open(input_file, 'r') as file:
    data = json.load(file)

ports = {}
ships = {}

# Парсимо вхідні дані і створюємо відповідні об'єкти
for item in data:
    if item['type'] == 'port':
        ports[item['id']] = Port(item['id'], item['latitude'], item['longitude'])
    elif item['type'] == 'ship':
        ships[item['id']] = Ship(item['id'], item['fuel'], ports[item['port_id']], item['total_capacity'],
                                 item['max_all'], item['max_heavy'], item['max_refrigerated'], item['max_liquid'],
                                 item['fuel_per_km'])
        ports[item['port_id']].incoming_ship(ships[item['id']])
    elif item['type'] == 'container':
        item_obj = ItemFactory.create_item(item['item_type'], item['item']['id'], item['item']['weight'],
                                           item['item']['count'], item['id'])
        container = Container(item['id'], item['weight'], item['container_type'], item_obj)
        ports[item['port_id']].add_container(container)
    elif item['type'] == 'operation':
        operation = item['action']
        if operation == "load":
            ship = ships[item['ship_id']]
            container = next(c for c in ports[item['port_id']].containers if c.id == item['container_id'])
            ship.load_container(container)
        elif operation == "unload":
            ship = ships[item['ship_id']]
            container = next(c for c in ship.containers if c.id == item['container_id'])
            ship.unload_container(container)
        elif operation == "sail":
            ship = ships[item['ship_id']]
            destination_port_id = item.get('destination_port_id')
            if destination_port_id in ports:
                destination_port = ports[destination_port_id]
                ship.sail(destination_port)
            else:
                print(f"Error: Port {destination_port_id} not found.")
                continue

# Серіалізація результатів
output_data = {
    'ports': [port.to_dict() for port in ports.values()],
    'ships': [ship.to_dict() for ship in ships.values()],  # Використовуємо to_dict() для серіалізації
}

with open(output_file, 'w') as file:
    json.dump(output_data, file, indent=4)

print("Data has been processed and saved to output.json.")
