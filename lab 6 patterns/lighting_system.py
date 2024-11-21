# lighting_system.py
class LightingSystem:
    def __init__(self):
        self.state = "off"
        self.brightness = 100

    def turnOnLights(self):
        self.state = "on"
        print("Lights turned on")

    def turnOffLights(self):
        self.state = "off"
        print("Lights turned off")

    def setBrightness(self, level):
        self.brightness = level
        print(f"Brightness set to {level}")
