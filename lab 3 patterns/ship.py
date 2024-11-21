class Ship:
    def __init__(self, id, fuel, port, total_capacity, max_all, max_heavy, max_refrigerated, max_liquid, fuel_per_km):
        self.id = id
        self.fuel = fuel
        self.port = port
        self.total_capacity = total_capacity
        self.max_all = max_all
        self.max_heavy = max_heavy
        self.max_refrigerated = max_refrigerated
        self.max_liquid = max_liquid
        self.fuel_per_km = fuel_per_km
        self.containers = []

    def load_container(self, container):
        self.containers.append(container)

    def unload_container(self, container):
        self.containers.remove(container)

    def sail(self, destination_port):
        self.port = destination_port

    def to_dict(self):
        return {
            "id": self.id,
            "fuel": self.fuel,
            "port_id": self.port.id if self.port else None,
            "total_capacity": self.total_capacity,
            "max_all": self.max_all,
            "max_heavy": self.max_heavy,
            "max_refrigerated": self.max_refrigerated,
            "max_liquid": self.max_liquid,
            "fuel_per_km": self.fuel_per_km,
            "containers": [container.to_dict() for container in self.containers],
        }
