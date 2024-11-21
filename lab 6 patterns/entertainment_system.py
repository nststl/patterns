# entertainment_system.py
class EntertainmentSystem:
    def __init__(self):
        self.state = "off"

    def playMusic(self):
        self.state = "on"
        print("Music playing")

    def stopMusic(self):
        self.state = "off"
        print("Music stopped")

    def setVolume(self, level):
        print(f"Volume set to {level}")
