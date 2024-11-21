# item.py

from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, ID, weight, count, containerID):
        self.ID = ID
        self.weight = weight
        self.count = count
        self.containerID = containerID

    @abstractmethod
    def getTotalWeight(self):
        pass

    def __repr__(self):
        return f"Item(ID={self.ID}, weight={self.weight}, count={self.count}, containerID={self.containerID})"

# Конкретні типи товарів
class SmallItem(Item):
    def __init__(self, ID, weight, count, containerID):
        super().__init__(ID, weight, count, containerID)

    def getTotalWeight(self):
        return self.weight * self.count


class HeavyItem(Item):
    def __init__(self, ID, weight, count, containerID):
        super().__init__(ID, weight, count, containerID)

    def getTotalWeight(self):
        return self.weight * self.count


class RefrigeratedItem(Item):
    def __init__(self, ID, weight, count, containerID):
        super().__init__(ID, weight, count, containerID)

    def getTotalWeight(self):
        return self.weight * self.count


class LiquidItem(Item):
    def __init__(self, ID, weight, count, containerID):
        super().__init__(ID, weight, count, containerID)

    def getTotalWeight(self):
        return self.weight * self.count


# Фабрика для створення товару (Item)
class ItemFactory:
    @staticmethod
    def create_item(item_type, ID, weight, count, containerID):
        if item_type == "small":
            return SmallItem(ID, weight, count, containerID)
        elif item_type == "heavy":
            return HeavyItem(ID, weight, count, containerID)
        elif item_type == "refrigerated":
            return RefrigeratedItem(ID, weight, count, containerID)
        elif item_type == "liquid":
            return LiquidItem(ID, weight, count, containerID)
        else:
            raise ValueError(f"Unknown item type: {item_type}")
