# settings_manager.py
class SettingsManager:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(SettingsManager, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.preferred_temperature = 72
            self.lighting_preset = 'medium'
            self.initialized = True

    def get_settings(self):
        return {
            "preferred_temperature": self.preferred_temperature,
            "lighting_preset": self.lighting_preset
        }
