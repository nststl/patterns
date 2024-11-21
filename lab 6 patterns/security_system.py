# security_system.py
class SecuritySystem:
    def __init__(self):
        self.armed = False

    def armSystem(self):
        self.armed = True
        print("Security system armed")

    def disarmSystem(self):
        self.armed = False
        print("Security system disarmed")

    def triggerAlarm(self):
        print("Alarm triggered!")
