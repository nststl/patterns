# smart_home_facade.py
from lighting_system import LightingSystem
from security_system import SecuritySystem
from climate_control_system import ClimateControlSystem
from entertainment_system import EntertainmentSystem

class SmartHomeFacade:
    def __init__(self):
        self.lighting = LightingSystem()
        self.security = SecuritySystem()
        self.climate = ClimateControlSystem()
        self.entertainment = EntertainmentSystem()

    def activateSecuritySystem(self):
        self.security.armSystem()

    def setClimateControl(self, target_temp):
        self.climate.setTemperature(target_temp)

    def controlLighting(self, state, brightness=None):
        if state == "on":
            self.lighting.turnOnLights()
            if brightness:
                self.lighting.setBrightness(brightness)
        elif state == "off":
            self.lighting.turnOffLights()
