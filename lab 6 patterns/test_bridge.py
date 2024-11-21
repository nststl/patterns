from tv_appliance import TVAppliance
from ac_appliance import ACAppliance
from remote_controller import RemoteController

def test_bridge_pattern():
    tv = TVAppliance()
    ac = ACAppliance()

    tv_remote = RemoteController(tv)
    ac_remote = RemoteController(ac)

    tv_remote.turn_on()
    tv_remote.turn_off()

    ac_remote.turn_on()
    ac_remote.turn_off()

test_bridge_pattern()
