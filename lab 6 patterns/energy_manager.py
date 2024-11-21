# energy_manager.py
class EnergyManager:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(EnergyManager, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.energy_usage = 0
            self.initialized = True

    def monitorUsage(self):
        print(f"Current energy usage: {self.energy_usage} kWh")

    def optimizeEnergy(self):
        self.energy_usage -= 1
        print(f"Energy optimized. Current usage: {self.energy_usage} kWh")
