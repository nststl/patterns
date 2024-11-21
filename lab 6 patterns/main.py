# main.py
from smart_home_facade import SmartHomeFacade
from voice_control import VoiceControl
from settings_manager import SettingsManager
from energy_manager import EnergyManager

def test_smart_home_system():
    # Create facade and voice control instances
    facade = SmartHomeFacade()
    voice_control = VoiceControl(facade)

    # Control the system via the facade
    facade.controlLighting("on", brightness=50)
    facade.setClimateControl(72)
    facade.activateSecuritySystem()

    # Test singleton pattern for SettingsManager and EnergyManager
    settings1 = SettingsManager()
    settings2 = SettingsManager()
    print("Are SettingsManager instances same?", settings1 is settings2)

    energy1 = EnergyManager()
    energy2 = EnergyManager()
    print("Are EnergyManager instances same?", energy1 is energy2)

    # Test voice control
    voice_control.processCommand("turn on lights")
    voice_control.processCommand("set temperature 75")

test_smart_home_system()
