from appliance import Appliance

class ACAppliance(Appliance):
    def start(self):
        print("AC is now ON")

    def stop(self):
        print("AC is now OFF")
