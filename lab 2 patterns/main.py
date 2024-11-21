from abc import ABC, abstractmethod

class Container(ABC):
    def __init__(self, ID, weight):
        self._ID = ID
        self._weight = weight

    @abstractmethod
    def consumption(self):
        pass

    def get_id(self):
        return self._ID

    def get_weight(self):
        return self._weight

    def __eq__(self, other): #порівнюємо id weight
        return isinstance(other, Container) and self._ID == other.get_id() and self._weight == other.get_weight()

class BasicContainer(Container):
    def __init__(self, ID, weight):
        super().__init__(ID, weight)

    def consumption(self):
        return self._weight * 2.5

class HeavyContainer(Container):
    def __init__(self, ID, weight):
        super().__init__(ID, weight)

    def consumption(self):
        return self._weight * 3.0

class RefrigeratedContainer(HeavyContainer):
    def consumption(self):
        return self._weight * 5.0

class LiquidContainer(HeavyContainer):
    def consumption(self):
        return self._weight * 4.0

class Port:
    def __init__(self, ID, latitude, longitude):
        self.ID = ID
        self.latitude = latitude
        self.longitude = longitude
        self.containers = []
        self.history = []
        self.current_ships = []

    def incoming_ship(self, ship):
        if ship not in self.current_ships:
            self.current_ships.append(ship)
        if ship not in self.history:
            self.history.append(ship)

    def outgoing_ship(self, ship):
        if ship in self.current_ships:
            self.current_ships.remove(ship)

    def get_distance(self, other_port):
        return ((self.latitude - other_port.latitude) ** 2 + (self.longitude - other_port.longitude) ** 2) ** 0.5

class Ship:
    def __init__(self, ID, fuel, port, total_capacity, max_all_containers, max_heavy, max_refrigerated, max_liquid, fuel_consumption_per_km):
        self.ID = ID
        self.fuel = fuel
        self.port = port
        self.total_capacity = total_capacity
        self.max_all_containers = max_all_containers
        self.max_heavy = max_heavy
        self.max_refrigerated = max_refrigerated
        self.max_liquid = max_liquid
        self.fuel_consumption_per_km = fuel_consumption_per_km
        self.containers = []

    def sail_to(self, destination_port):
        distance = self.port.get_distance(destination_port)
        required_fuel = distance * self.fuel_consumption_per_km + sum(c.consumption() for c in self.containers)
        if self.fuel >= required_fuel:
            self.fuel -= required_fuel
            self.port.outgoing_ship(self)
            destination_port.incoming_ship(self)
            self.port = destination_port
            return True
        return False

    def load(self, container):
        if isinstance(container, BasicContainer) and len(self.containers) < self.max_all_containers:
            self.containers.append(container)
            return True
        # Further checks for container limits and type restrictions
        return False

    def unload(self, container):
        if container in self.containers:
            self.containers.remove(container)
            self.port.containers.append(container)
            return True
        return False

    def refuel(self, amount):
        self.fuel += amount

    def get_current_containers(self):
        return sorted(self.containers, key=lambda c: c.get_id())

import json

input_file='input.json'
output_file='output.json'

with open(input_file, 'r') as file:
    data = json.load(file)

ports = {}
ships = {}

# Parse and create objects based on JSON data
for item in data:
    if item['type'] == 'port':
         ports[item['id']] = Port(item['id'], item['latitude'], item['longitude'])
    elif item['type'] == 'ship':
        ports[item['port_id']].incoming_ship(
            Ship(item['id'], item['fuel'], ports[item['port_id']], item['total_capacity'],
                    item['max_all'], item['max_heavy'], item['max_refrigerated'], item['max_liquid'],
                    item['fuel_per_km']))
    elif item['type'] == 'container':
        # Handling container creation based on weight and type
        pass
    # Handle load, unload, sail, refuel actions

def serialize_ports(ports):
    serialized = {}
    for port_id, port in ports.items():
        serialized[port_id] = {
            "id": port.ID,
            "latitude": port.latitude,
            "longitude": port.longitude,
            "containers": [c.get_id() for c in port.containers],
            "history": [s.ID for s in port.history],
            "current_ships": [s.ID for s in port.current_ships]
        }
    return serialized

def serialize_ships(ships):
    serialized = {}
    for ship_id, ship in ships.items():
        serialized[ship_id] = {
            "id": ship.ID,
            "fuel": ship.fuel,
            "port_id": ship.port.ID if ship.port else None,
            "containers": [c.get_id() for c in ship.containers]
        }
    return serialized

# Серіалізація об'єктів
output_data = {
    "ports": serialize_ports(ports),
    "ships": serialize_ships(ships)
}

# Збереження у файл
with open(output_file, 'w') as file:
    json.dump(output_data, file, indent=2)





