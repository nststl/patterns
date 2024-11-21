from appliance import Appliance

class TVAppliance(Appliance):
    def start(self):
        print("TV is now ON")

    def stop(self):
        print("TV is now OFF")
