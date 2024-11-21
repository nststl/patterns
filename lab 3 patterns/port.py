

class Port:
    def __init__(self, id, latitude, longitude):
        self.id = id
        self.latitude = latitude
        self.longitude = longitude
        self.containers = []
        self.ships = []

    def add_container(self, container):
        self.containers.append(container)

    def incoming_ship(self, ship):
        self.ships.append(ship)

    def to_dict(self):
        return {
            "id": self.id,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "containers": [container.to_dict() for container in self.containers],
            "ships": [ship.to_dict() for ship in self.ships],
        }
