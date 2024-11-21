class Container:
    def __init__(self, id, weight, container_type, item):
        self.id = id
        self.weight = weight
        self.container_type = container_type
        self.item = item

    def to_dict(self):
        return {
            "id": self.id,
            "weight": self.weight,
            "container_type": self.container_type,
            "item": self.item.to_dict() if self.item else None
        }
