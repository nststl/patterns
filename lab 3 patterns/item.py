# item.py

class Item:
    def __init__(self, id, weight, count, container_id):
        self.id = id
        self.weight = weight
        self.count = count
        self.container_id = container_id

    def to_dict(self):
        return {
            "id": self.id,
            "weight": self.weight,
            "count": self.count,
            "container_id": self.container_id
        }

# Підкласи для різних типів товарів
class SmallItem(Item):
    def __init__(self, id, weight, count, container_id):
        super().__init__(id, weight, count, container_id)
        self.item_type = "small"

    def to_dict(self):
        item_dict = super().to_dict()
        item_dict["item_type"] = self.item_type
        return item_dict

class HeavyItem(Item):
    def __init__(self, id, weight, count, container_id):
        super().__init__(id, weight, count, container_id)
        self.item_type = "heavy"

    def to_dict(self):
        item_dict = super().to_dict()
        item_dict["item_type"] = self.item_type
        return item_dict

class RefrigeratedItem(Item):
    def __init__(self, id, weight, count, container_id):
        super().__init__(id, weight, count, container_id)
        self.item_type = "refrigerated"

    def to_dict(self):
        item_dict = super().to_dict()
        item_dict["item_type"] = self.item_type
        return item_dict

class LiquidItem(Item):
    def __init__(self, id, weight, count, container_id):
        super().__init__(id, weight, count, container_id)
        self.item_type = "liquid"

    def to_dict(self):
        item_dict = super().to_dict()
        item_dict["item_type"] = self.item_type
        return item_dict


# Клас ItemFactory, який створює об'єкти типів Item
class ItemFactory:
    @staticmethod
    def create_item(item_type, id, weight, count, container_id):
        if item_type == 'small':
            return SmallItem(id, weight, count, container_id)
        elif item_type == 'heavy':
            return HeavyItem(id, weight, count, container_id)
        elif item_type == 'refrigerated':
            return RefrigeratedItem(id, weight, count, container_id)
        elif item_type == 'liquid':
            return LiquidItem(id, weight, count, container_id)
        else:
            raise ValueError(f"Unknown item type: {item_type}")
