# voice_control.py
class VoiceControl:
    def __init__(self, facade):
        self.facade = facade

    def processCommand(self, command: str):
        if "turn on lights" in command:
            self.facade.controlLighting("on")
        elif "turn off lights" in command:
            self.facade.controlLighting("off")
        elif "set temperature" in command:
            temp = int(command.split()[-1])  # Extract temperature from command
            self.facade.setClimateControl(temp)
        elif "arm security" in command:
            self.facade.activateSecuritySystem()
