# climate_control_system.py
class ClimateControlSystem:
    def __init__(self):
        self.temperature = 70

    def setTemperature(self, target_temp):
        self.temperature = target_temp
        print(f"Temperature set to {target_temp}°F")

    def turnOnHeater(self):
        print("Heater turned on")

    def turnOnAC(self):
        print("AC turned on")
